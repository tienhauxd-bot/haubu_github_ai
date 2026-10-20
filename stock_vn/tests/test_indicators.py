import os
import unittest

from stock_vn import indicators as ind
from stock_vn import sources
from stock_vn.sources import Fundamentals

HERE = os.path.dirname(__file__)


class TechnicalTest(unittest.TestCase):
    def test_rsi_extremes(self):
        self.assertEqual(ind.rsi([float(i) for i in range(1, 30)]), 100.0)
        self.assertLess(ind.rsi([float(i) for i in range(30, 1, -1)]), 1)

    def test_change_and_volume(self):
        closes = [100.0] * 60
        vols = [1000.0] * 59 + [3000.0]
        t = ind.technical(closes, vols, price=105.0)
        self.assertAlmostEqual(t.change_pct, 0.05)
        self.assertAlmostEqual(t.volume_ratio, 3.0)
        self.assertIsNotNone(t.sma50)


class FundamentalTest(unittest.TestCase):
    def good(self, **kw):
        base = dict(ticker="AAA", eps=5000, bvps=25000, roe=0.2, roa=0.08,
                    debt_on_equity=0.5, net_margin=0.15, eps_growth=0.1,
                    pe_history=[15, 16, 14])
        base.update(kw)
        return Fundamentals(**base)

    def test_valuation(self):
        v = ind.valuation(self.good(), price=50000)
        self.assertAlmostEqual(v.pe, 10)
        self.assertAlmostEqual(v.pb, 2)
        self.assertAlmostEqual(v.graham_value, (22.5 * 5000 * 25000) ** 0.5)
        self.assertAlmostEqual(v.margin_of_safety, 1 - 50000 / v.graham_value)
        self.assertEqual(v.quality_score, 1.0)

    def test_bank_skips_graham_uses_pe(self):
        f = self.good(is_bank=True, debt_on_equity=8, net_margin=None, roa=0.015)
        v = ind.valuation(f, price=50000)
        self.assertIsNone(v.graham_value)
        self.assertAlmostEqual(v.pe_discount, 1 - 10 / 15)
        self.assertEqual(v.quality_score, 1.0)  # nợ/VCSH không tính cho ngân hàng

    def test_signals(self):
        trend = [40000.0 + i * 100 for i in range(60)]
        vols = [1000.0] * 60
        cheap = ind.combine(ind.technical(trend, vols, 50000), ind.valuation(self.good(), 50000))
        self.assertTrue(cheap.label.startswith("VÙNG MUA"))
        pricey = ind.combine(ind.technical(trend, vols, 200000), ind.valuation(self.good(), 200000))
        self.assertTrue(pricey.label.startswith("ĐẮT"))
        junk = self.good(roe=0.03, roa=0.01, debt_on_equity=3, net_margin=0.02, eps_growth=-0.2)
        bad = ind.combine(ind.technical(trend, vols, 50000), ind.valuation(junk, 50000))
        self.assertTrue(bad.label.startswith("TRÁNH"))

    def test_missing_data(self):
        s = ind.combine(ind.technical([1.0], [1.0], 1.0), ind.valuation(Fundamentals("X"), 1.0))
        self.assertEqual(s.label, "THIẾU DỮ LIỆU")


class CsvTest(unittest.TestCase):
    def test_load_sample(self):
        funds = sources.load_fundamentals_csv(os.path.join(HERE, "..", "sample", "fundamentals.csv"))
        self.assertAlmostEqual(funds["FPT"].roe, 0.28)
        self.assertTrue(funds["VCB"].is_bank)
        self.assertIsNone(funds["VCB"].debt_on_equity)
        self.assertEqual(funds["FPT"].pe_history[0], 18)


if __name__ == "__main__":
    unittest.main()
