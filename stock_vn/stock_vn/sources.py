"""Nguồn dữ liệu.

- Giá: API chart công khai của DNSE (Entrade), không cần tài khoản. Nến 1 phút
  được cập nhật liên tục trong phiên nên poll mỗi 10-30 giây là gần realtime.
- Báo cáo tài chính: API phân tích công khai của TCBS (chỉ số theo quý/năm).
- Dự phòng: file CSV chỉ số tài chính tự nhập (xem sample/fundamentals.csv).

Các API công khai này không có cam kết chính thức, có thể đổi định dạng bất kỳ
lúc nào. Mọi chỗ đọc dữ liệu đều dùng .get() để thiếu trường thì trả về None.
"""

from __future__ import annotations

import csv
import time
from dataclasses import dataclass, field
from typing import Optional

import requests

DNSE_CHART_URL = "https://services.entrade.com.vn/chart-api/v2/ohlcs/stock"
TCBS_RATIO_URL = "https://apipubaws.tcbs.com.vn/tcanalysis/v1/finance/{ticker}/financialratio"

# DNSE trả giá theo đơn vị nghìn đồng (VD: 89.5 = 89.500đ).
DNSE_PRICE_UNIT = 1000

HEADERS = {"User-Agent": "Mozilla/5.0 (stock_vn)"}
TIMEOUT = 15


@dataclass
class Bars:
    """Chuỗi nến, giá tính bằng VND, cũ nhất trước."""

    time: list[int] = field(default_factory=list)
    open: list[float] = field(default_factory=list)
    high: list[float] = field(default_factory=list)
    low: list[float] = field(default_factory=list)
    close: list[float] = field(default_factory=list)
    volume: list[float] = field(default_factory=list)


@dataclass
class Fundamentals:
    """Chỉ số tài chính của một kỳ. Tỷ lệ lưu dạng thập phân (0.18 = 18%)."""

    ticker: str
    period: str = ""
    eps: Optional[float] = None  # VND, 4 quý gần nhất
    bvps: Optional[float] = None  # VND
    roe: Optional[float] = None
    roa: Optional[float] = None
    debt_on_equity: Optional[float] = None
    net_margin: Optional[float] = None
    eps_growth: Optional[float] = None  # so với cùng kỳ
    is_bank: bool = False
    # P/E lịch sử để so sánh định giá hiện tại với chính nó trong quá khứ.
    pe_history: list[float] = field(default_factory=list)


def _as_fraction(value) -> Optional[float]:
    """Chuẩn hoá tỷ lệ về dạng thập phân; chấp nhận cả 18 lẫn 0.18."""
    if value is None or value == "":
        return None
    v = float(value)
    return v / 100 if abs(v) > 1.5 else v


def _as_float(value) -> Optional[float]:
    if value is None or value == "":
        return None
    return float(value)


def fetch_bars(symbol: str, resolution: str = "1D", days: int = 120) -> Bars:
    """Lấy nến từ DNSE. resolution: "1" (1 phút), "15", "1H", "1D"."""
    now = int(time.time())
    params = {
        "symbol": symbol.upper(),
        "resolution": resolution,
        "from": now - days * 86400,
        "to": now,
    }
    r = requests.get(DNSE_CHART_URL, params=params, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    data = r.json()
    scale = lambda xs: [float(x) * DNSE_PRICE_UNIT for x in xs]  # noqa: E731
    return Bars(
        time=list(data.get("t", [])),
        open=scale(data.get("o", [])),
        high=scale(data.get("h", [])),
        low=scale(data.get("l", [])),
        close=scale(data.get("c", [])),
        volume=[float(v) for v in data.get("v", [])],
    )


def fetch_fundamentals_tcbs(symbol: str, yearly: bool = False) -> Fundamentals:
    """Lấy chỉ số tài chính từ TCBS; phần tử đầu là kỳ gần nhất."""
    url = TCBS_RATIO_URL.format(ticker=symbol.upper())
    params = {"yearly": 1 if yearly else 0, "isAll": "true"}
    r = requests.get(url, params=params, headers=HEADERS, timeout=TIMEOUT)
    r.raise_for_status()
    rows = r.json()
    if not rows:
        raise ValueError(f"TCBS không có dữ liệu tài chính cho {symbol}")
    latest = rows[0]
    period = f"Q{latest.get('quarter')}/{latest.get('year')}"
    pe_history = [float(x["priceToEarning"]) for x in rows if x.get("priceToEarning")]
    return Fundamentals(
        ticker=symbol.upper(),
        period=period,
        eps=_as_float(latest.get("earningPerShare")),
        bvps=_as_float(latest.get("bookValuePerShare")),
        roe=_as_fraction(latest.get("roe")),
        roa=_as_fraction(latest.get("roa")),
        debt_on_equity=_as_float(latest.get("debtOnEquity")),
        net_margin=_as_fraction(latest.get("postTaxMargin")),
        eps_growth=_as_fraction(latest.get("epsChange")),
        # Ngân hàng không có biên lãi gộp; dùng làm dấu hiệu nhận biết.
        is_bank=latest.get("grossProfitMargin") is None and latest.get("roe") is not None,
        pe_history=[p for p in pe_history if 0 < p < 200],
    )


def load_fundamentals_csv(path: str) -> dict[str, Fundamentals]:
    """Đọc chỉ số tài chính từ CSV (một dòng mỗi mã). Xem sample/fundamentals.csv."""
    out: dict[str, Fundamentals] = {}
    with open(path, newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            ticker = row["ticker"].strip().upper()
            pe_hist = [float(x) for x in (row.get("pe_history") or "").split("|") if x]
            out[ticker] = Fundamentals(
                ticker=ticker,
                period=row.get("period", ""),
                eps=_as_float(row.get("eps")),
                bvps=_as_float(row.get("bvps")),
                roe=_as_fraction(row.get("roe")),
                roa=_as_fraction(row.get("roa")),
                debt_on_equity=_as_float(row.get("debt_on_equity")),
                net_margin=_as_fraction(row.get("net_margin")),
                eps_growth=_as_fraction(row.get("eps_growth")),
                is_bank=(row.get("is_bank") or "").strip().lower() in ("1", "true", "yes"),
                pe_history=pe_hist,
            )
    return out
