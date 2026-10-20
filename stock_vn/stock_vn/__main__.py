"""Dòng lệnh.

    python -m stock_vn watch FPT VCB HPG --interval 15
    python -m stock_vn watch FPT --fundamentals sample/fundamentals.csv --once
"""

from __future__ import annotations

import argparse
import sys
import time
from datetime import datetime

from . import indicators as ind
from . import sources


def _fmt_vnd(x) -> str:
    return "—" if x is None else f"{x:,.0f}đ"


def _fmt(x, digits: int) -> str:
    return "—" if x is None else f"{x:.{digits}f}"


def analyze(symbol: str, fund: sources.Fundamentals) -> str:
    daily = sources.fetch_bars(symbol, "1D", days=120)
    minute = sources.fetch_bars(symbol, "1", days=1)
    if not daily.close:
        raise ValueError("không có dữ liệu giá")
    price = minute.close[-1] if minute.close else daily.close[-1]
    today_vol = sum(minute.volume) if minute.volume else None

    t = ind.technical(daily.close, daily.volume, price, today_vol)
    v = ind.valuation(fund, price)
    s = ind.combine(t, v)

    chg = "—" if t.change_pct is None else f"{t.change_pct:+.2%}"
    lines = [
        f"■ {symbol}  {_fmt_vnd(price)} ({chg})   ⇒ {s.label}",
        f"  P/E {_fmt(v.pe, 1)} | P/B {_fmt(v.pb, 2)} | Graham {_fmt_vnd(v.graham_value)}"
        f" | RSI {_fmt(t.rsi14, 0)} | KL/TB20 {_fmt(t.volume_ratio, 2)}"
        f" | BCTC {fund.period}",
    ]
    lines += [f"  · {r}" for r in s.reasons]
    lines += [f"  ! {a}" for a in s.alerts]
    lines += [f"    {n}" for n in v.quality_notes]
    return "\n".join(lines)


def cmd_watch(args) -> int:
    csv_funds = sources.load_fundamentals_csv(args.fundamentals) if args.fundamentals else {}
    funds: dict[str, sources.Fundamentals] = {}
    for sym in (s.upper() for s in args.symbols):
        if sym in csv_funds:
            funds[sym] = csv_funds[sym]
            continue
        try:
            funds[sym] = sources.fetch_fundamentals_tcbs(sym)
        except Exception as e:  # BCTC đổi theo quý nên chỉ cần lấy một lần
            print(f"[{sym}] không lấy được BCTC từ TCBS: {e}", file=sys.stderr)
            funds[sym] = sources.Fundamentals(ticker=sym)

    while True:
        print(f"\n===== {datetime.now():%Y-%m-%d %H:%M:%S} =====")
        for sym, fund in funds.items():
            try:
                print(analyze(sym, fund))
            except Exception as e:
                print(f"■ {sym}: lỗi lấy giá – {e}")
        if args.once:
            return 0
        time.sleep(args.interval)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="stock_vn", description="Chỉ báo cổ phiếu VN: giá realtime + BCTC")
    sub = p.add_subparsers(dest="cmd", required=True)
    w = sub.add_parser("watch", help="theo dõi danh sách mã")
    w.add_argument("symbols", nargs="+")
    w.add_argument("--interval", type=int, default=15, help="số giây giữa các lần cập nhật")
    w.add_argument("--fundamentals", help="CSV chỉ số tài chính (ghi đè dữ liệu TCBS)")
    w.add_argument("--once", action="store_true", help="chạy một lần rồi thoát")
    w.set_defaults(func=cmd_watch)
    args = p.parse_args(argv)
    try:
        return args.func(args)
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
