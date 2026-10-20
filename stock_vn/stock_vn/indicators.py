"""Chỉ báo: kỹ thuật (biến động giá), cơ bản (BCTC) và tín hiệu kết hợp."""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from typing import Optional

from .sources import Fundamentals


# ---------------------------------------------------------------- kỹ thuật


def sma(values: list[float], n: int) -> Optional[float]:
    if len(values) < n:
        return None
    return sum(values[-n:]) / n


def rsi(closes: list[float], n: int = 14) -> Optional[float]:
    """RSI theo cách làm mượt của Wilder."""
    if len(closes) <= n:
        return None
    gains, losses = [], []
    for prev, cur in zip(closes, closes[1:]):
        d = cur - prev
        gains.append(max(d, 0.0))
        losses.append(max(-d, 0.0))
    avg_gain = sum(gains[:n]) / n
    avg_loss = sum(losses[:n]) / n
    for g, l in zip(gains[n:], losses[n:]):
        avg_gain = (avg_gain * (n - 1) + g) / n
        avg_loss = (avg_loss * (n - 1) + l) / n
    if avg_loss == 0:
        return 100.0
    return 100 - 100 / (1 + avg_gain / avg_loss)


@dataclass
class Technical:
    price: float
    ref_price: Optional[float]  # giá đóng cửa phiên trước
    change_pct: Optional[float]
    sma20: Optional[float]
    sma50: Optional[float]
    rsi14: Optional[float]
    volume_ratio: Optional[float]  # KL hôm nay / TB 20 phiên trước


def technical(daily_close: list[float], daily_volume: list[float], price: float,
              today_volume: Optional[float] = None) -> Technical:
    """daily_close/daily_volume: nến ngày, phần tử cuối là phiên hôm nay (nếu đang giao dịch).

    price: giá khớp mới nhất (lấy từ nến phút để gần realtime).
    """
    closes = list(daily_close)
    if closes:
        closes[-1] = price
    ref = daily_close[-2] if len(daily_close) >= 2 else None
    change = (price / ref - 1) if ref else None
    vol_today = today_volume if today_volume is not None else (daily_volume[-1] if daily_volume else None)
    past = daily_volume[-21:-1]
    vol_ratio = (vol_today / (sum(past) / len(past))) if vol_today and past and sum(past) else None
    return Technical(
        price=price,
        ref_price=ref,
        change_pct=change,
        sma20=sma(closes, 20),
        sma50=sma(closes, 50),
        rsi14=rsi(closes, 14),
        volume_ratio=vol_ratio,
    )


# ---------------------------------------------------------------- cơ bản


@dataclass
class Valuation:
    pe: Optional[float]
    pb: Optional[float]
    pe_median: Optional[float]  # P/E trung vị lịch sử của chính mã này
    pe_discount: Optional[float]  # >0: rẻ hơn trung vị lịch sử
    graham_value: Optional[float]
    margin_of_safety: Optional[float]  # (giá trị - giá) / giá trị
    quality_score: Optional[float]  # 0..1
    quality_notes: list[str] = field(default_factory=list)


def quality(f: Fundamentals) -> tuple[Optional[float], list[str]]:
    """Chấm điểm chất lượng doanh nghiệp. Bỏ qua tiêu chí thiếu dữ liệu."""
    checks: list[tuple[bool, str]] = []
    if f.roe is not None:
        checks.append((f.roe >= 0.15, f"ROE {f.roe:.1%} {'≥' if f.roe >= 0.15 else '<'} 15%"))
    if f.roa is not None:
        bar = 0.01 if f.is_bank else 0.05
        checks.append((f.roa >= bar, f"ROA {f.roa:.1%} (ngưỡng {bar:.0%})"))
    if f.debt_on_equity is not None and not f.is_bank:
        checks.append((f.debt_on_equity <= 1.0, f"Nợ/VCSH {f.debt_on_equity:.2f} (ngưỡng 1.0)"))
    if f.net_margin is not None and not f.is_bank:
        checks.append((f.net_margin >= 0.10, f"Biên LN ròng {f.net_margin:.1%} (ngưỡng 10%)"))
    if f.eps_growth is not None:
        checks.append((f.eps_growth > 0, f"Tăng trưởng EPS {f.eps_growth:+.1%}"))
    if not checks:
        return None, ["Thiếu dữ liệu BCTC"]
    score = sum(ok for ok, _ in checks) / len(checks)
    notes = [("✓ " if ok else "✗ ") + text for ok, text in checks]
    return score, notes


def valuation(f: Fundamentals, price: float) -> Valuation:
    pe = price / f.eps if f.eps and f.eps > 0 else None
    pb = price / f.bvps if f.bvps and f.bvps > 0 else None
    pe_median = statistics.median(f.pe_history) if f.pe_history else None
    pe_discount = (1 - pe / pe_median) if pe and pe_median else None
    # Graham number: giá trị hợp lý thận trọng; với ngân hàng dùng P/B nên bỏ qua.
    graham = None
    if not f.is_bank and f.eps and f.bvps and f.eps > 0 and f.bvps > 0:
        graham = math.sqrt(22.5 * f.eps * f.bvps)
    mos = (graham - price) / graham if graham else None
    score, notes = quality(f)
    return Valuation(pe, pb, pe_median, pe_discount, graham, mos, score, notes)


# ---------------------------------------------------------------- kết hợp


@dataclass
class Signal:
    label: str
    reasons: list[str]
    alerts: list[str]


def combine(t: Technical, v: Valuation) -> Signal:
    """Định giá + chất lượng quyết định "mua gì", biến động giá quyết định "khi nào"."""
    reasons: list[str] = []
    alerts: list[str] = []

    # Thước đo "rẻ": ưu tiên so P/E với lịch sử của chính mã đó. Graham quá khắt khe
    # với doanh nghiệp ROE cao nên chỉ dùng khi không có lịch sử P/E.
    cheapness = v.pe_discount if v.pe_discount is not None else v.margin_of_safety
    if v.margin_of_safety is not None:
        reasons.append(f"Biên an toàn Graham {v.margin_of_safety:+.0%}")
    if v.pe_discount is not None:
        reasons.append(f"P/E {v.pe:.1f} so với trung vị {v.pe_median:.1f} ({v.pe_discount:+.0%})")
    if v.quality_score is not None:
        reasons.append(f"Điểm chất lượng {v.quality_score:.0%}")

    uptrend = t.sma50 is not None and t.price > t.sma50
    oversold = t.rsi14 is not None and t.rsi14 < 30
    overbought = t.rsi14 is not None and t.rsi14 > 70

    if v.quality_score is not None and v.quality_score < 0.4:
        label = "TRÁNH – chất lượng thấp"
    elif cheapness is None or v.quality_score is None:
        label = "THIẾU DỮ LIỆU"
    elif cheapness >= 0.3:
        label = "VÙNG MUA – rẻ & chất lượng" if uptrend or oversold else "RẺ – chờ xu hướng xác nhận"
    elif cheapness >= 0.1:
        label = "THEO DÕI – định giá hợp lý"
    elif cheapness >= -0.1:
        label = "NẮM GIỮ – sát giá trị"
    else:
        label = "ĐẮT – vượt giá trị nội tại"

    if (t.volume_ratio is not None and t.volume_ratio >= 2
            and t.change_pct is not None and abs(t.change_pct) >= 0.02):
        side = "mua" if t.change_pct > 0 else "bán"
        alerts.append(f"Dòng tiền đột biến: KL gấp {t.volume_ratio:.1f}x TB20, lực {side} {t.change_pct:+.1%}")
    if t.change_pct is not None and abs(t.change_pct) >= 0.05:
        alerts.append(f"Biến động mạnh trong phiên {t.change_pct:+.1%}")
    if oversold:
        alerts.append(f"RSI {t.rsi14:.0f} – quá bán")
    if overbought:
        alerts.append(f"RSI {t.rsi14:.0f} – quá mua")
    if cheapness is not None and cheapness >= 0.3 and t.change_pct is not None and t.change_pct <= -0.03:
        alerts.append("Cổ phiếu tốt đang giảm sâu → cơ hội gia tăng biên an toàn")

    return Signal(label, reasons, alerts)
