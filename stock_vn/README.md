# stock_vn: Giá realtime + Báo cáo tài chính → Chỉ báo

Công cụ dòng lệnh theo dõi cổ phiếu Việt Nam. Nó lấy **giá khớp lệnh gần realtime** rồi kết hợp với **chỉ số từ báo cáo tài chính** để ra tín hiệu theo trường phái đầu tư giá trị:

- **BCTC trả lời "mua cái gì"**: doanh nghiệp có chất lượng không, đang rẻ hay đắt so với giá trị.
- **Biến động giá trả lời "khi nào"**: xu hướng, quá mua/quá bán, dòng tiền đột biến.

## Cài đặt & chạy

Yêu cầu Python 3.9+ và mạng Internet tại Việt Nam (hoặc mạng không chặn các API dưới đây).

```bash
cd stock_vn
pip install -r requirements.txt

# Theo dõi liên tục, cập nhật mỗi 15 giây (Ctrl+C để dừng)
python -m stock_vn watch FPT VCB HPG MWG --interval 15

# Chạy một lần
python -m stock_vn watch FPT --once

# Dùng số liệu BCTC tự nhập (ghi đè dữ liệu TCBS)
python -m stock_vn watch FPT VCB --fundamentals sample/fundamentals.csv
```

Ví dụ kết quả:

```
■ VCB  61,837đ (+0.27%)   ⇒ VÙNG MUA – rẻ & chất lượng
  P/E 10.3 | P/B 1.77 | Graham — | RSI 56 | KL/TB20 2.11 | BCTC Q2/2026
  · P/E 10.3 so với trung vị 15.5 (+34%)
  · Điểm chất lượng 100%
    ✓ ROE 19.0% ≥ 15%
    ✓ ROA 1.7% (ngưỡng 1%)
    ✓ Tăng trưởng EPS +8.0%
```

## Nguồn dữ liệu (miễn phí, không cần tài khoản)

| Dữ liệu | Nguồn | Độ trễ |
|---|---|---|
| Giá khớp, khối lượng | API chart công khai DNSE (nến 1 phút + nến ngày) | vài giây đến ~1 phút |
| Chỉ số tài chính (EPS, BVPS, ROE, ROA, Nợ/VCSH, P/E lịch sử…) | API phân tích công khai TCBS | cập nhật theo quý |
| Dự phòng | File CSV tự nhập (`sample/fundamentals.csv`) | — |

> Đây là các API công khai, không có cam kết chính thức nên có thể đổi bất kỳ lúc nào. Nếu một nguồn lỗi, công cụ báo lỗi cho mã đó và vẫn chạy tiếp các mã khác. Nếu cần dữ liệu từng lệnh khớp (tick) thật sự, nên dùng **SSI FastConnect Data** hoặc **DNSE Market Data (MQTT)**. Cả hai miễn phí cho người có tài khoản, và có thể viết thêm adapter trong `stock_vn/sources.py`.
>
> Thư viện `vnstock` hiện đang bị PyPI cách ly (quarantined) nên công cụ này không dùng nó.

## Các chỉ báo

**Kỹ thuật (từ giá):** % thay đổi so với tham chiếu, SMA20, SMA50, RSI14, khối lượng hôm nay so với trung bình 20 phiên.

**Cơ bản (từ BCTC + giá realtime):**
- P/E, P/B tính theo giá hiện tại.
- **P/E so với trung vị lịch sử** của chính mã đó: rẻ hay đắt so với chính nó.
- **Graham number** = √(22,5 × EPS × BVPS) và biên an toàn. Không áp dụng cho ngân hàng.
- **Điểm chất lượng** (0–100%): ROE ≥ 15%, ROA ≥ 5% (ngân hàng ≥ 1%), Nợ/VCSH ≤ 1, biên LN ròng ≥ 10%, EPS tăng trưởng dương. Ngân hàng bỏ qua tiêu chí nợ và biên LN.

**Tín hiệu kết hợp:**

| Nhãn | Điều kiện |
|---|---|
| TRÁNH – chất lượng thấp | Điểm chất lượng < 40% |
| VÙNG MUA – rẻ & chất lượng | Rẻ ≥ 30% **và** (giá trên SMA50 hoặc RSI < 30) |
| RẺ – chờ xu hướng xác nhận | Rẻ ≥ 30% nhưng xu hướng còn yếu |
| THEO DÕI – định giá hợp lý | Rẻ 10–30% |
| NẮM GIỮ – sát giá trị | Rẻ/đắt trong khoảng ±10% |
| ĐẮT – vượt giá trị nội tại | Đắt hơn 10% |

"Rẻ" là mức chiết khấu P/E so với trung vị lịch sử; nếu không có lịch sử P/E thì dùng biên an toàn Graham.

**Cảnh báo trong phiên:** khối lượng ≥ 2 lần TB20 kèm giá biến động ≥ 2%, biến động ≥ 5%, RSI quá mua/quá bán, và cổ phiếu rẻ đang giảm sâu (cơ hội tăng biên an toàn).

Có thể sửa các ngưỡng trong `stock_vn/indicators.py`.

## File CSV tự nhập

```
ticker,period,eps,bvps,roe,roa,debt_on_equity,net_margin,eps_growth,is_bank,pe_history
FPT,Q2/2026,5200,22000,28,12,0.9,15,20,0,18|20|22|19|17|21
```

EPS và BVPS tính bằng VND. Các tỷ lệ nhập dạng % (28) hoặc thập phân (0.28) đều được. `pe_history` là các mức P/E quá khứ, ngăn cách bằng `|`. Ô trống thì tiêu chí đó được bỏ qua. Số liệu trong `sample/fundamentals.csv` chỉ là ví dụ, không phải số thật.

## Kiểm thử

```bash
python -m unittest discover -s tests -v
```

## Lưu ý

Công cụ chỉ hỗ trợ phân tích, **không phải khuyến nghị mua bán**. Dữ liệu từ nguồn công khai có thể trễ hoặc sai. Nếu muốn hiển thị lại dữ liệu realtime công khai trên website, bạn cần có bản quyền dữ liệu từ HOSE/HNX.
