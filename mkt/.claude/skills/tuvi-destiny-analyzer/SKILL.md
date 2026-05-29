---
name: tuvi-destiny-analyzer
description: "Phân tích lá số Tử Vi đầy đủ, chuyên sâu theo phương pháp Tam Hợp Nam Phái từ cuốn Mệnh Lý Thiên Cơ (Lê Quang Lăng). USE WHEN user nói 'phân tích lá số', 'xem tử vi', 'đọc lá số', 'luận mệnh', 'phân tích lá số của tôi', 'xem mệnh', 'tử vi của tôi', 'đưa lá số lên', 'phân tích vận mệnh', 'xem vận hạn', 'phân tích cung mệnh'."
---

# Tử Vi Destiny Analyzer — Phân Tích Lá Số Toàn Diện

Phân tích lá số Tử Vi chuyên sâu theo **Tam Hợp Nam Phái** dựa trên kiến thức từ `TV34_TuViNamPhai_Full.md` (cuốn Mệnh Lý Thiên Cơ ~900 trang). Áp dụng đúng trình tự 7 bước suy luận của chuyên gia.

**Nguồn tham chiếu chính**: `TV34_TuViNamPhai_Full.md` trong thư mục dự án.

---

## Khi nào dùng

- User cung cấp lá số Tử Vi (ảnh, text, hoặc thông tin bát tự)
- Muốn phân tích tổng quan mệnh lý (tính cách, sự nghiệp, tài lộc, tình cảm)
- Muốn xem vận hạn hiện tại (Đại Hạn + Lưu Niên 2026)
- Muốn nhận dạng cách cục và tiên đoán xu hướng

---

## Input — Cách nhận lá số

**Chấp nhận 3 định dạng đầu vào:**

### Format A — Ảnh lá số
User upload ảnh lá số tử vi. Từ ảnh, đọc và extract:
- Cung Mệnh nằm ở ô nào (12 cung theo chiều ngược kim đồng hồ từ Dần)
- 14 chính tinh nằm ở cung nào
- Các phụ tinh quan trọng (Tứ Hóa, sát tinh, cát tinh)
- Thông tin năm sinh, Ngũ Hành Cục, Mệnh Chủ, Thân Chủ

### Format B — Text mô tả
User cung cấp text theo mẫu:
```
Năm sinh: [Can Chi] (VD: Giáp Tý)
Giới tính: Nam/Nữ
Ngũ Hành Cục: [VD: Mộc Tam Cục]
Cung Mệnh: [cung + địa chi] (VD: Mệnh tại Ngọ)
Đại Hạn hiện tại: [VD: Hạn Tỵ, 2022–2032]

Bố trí 12 cung (liệt kê từng cung):
- Tý: [các sao]
- Sửu: [các sao]
- Dần: [các sao]
...
```

### Format C — Bát Tự
Nếu user chỉ cung cấp ngày giờ sinh:
- Ngày/Tháng/Năm sinh (dương lịch hoặc âm lịch)
- Giờ sinh (giờ âm lịch hoặc tên giờ: Tý, Sửu, Dần...)
- Giới tính

→ Từ bát tự, xác định Ngũ Hành Cục → an sao cơ bản → lập cung Mệnh trước khi phân tích.

**Nếu thiếu thông tin**: Hỏi user bổ sung trước khi phân tích.

---

## Process — 7 Bước Suy Luận

### BƯỚC 1 — Xác lập Nền Tảng Lá Số

**Đọc từ `TV34_TuViNamPhai_Full.md` phần Chương I §3–7**

Xác định và ghi rõ:
1. **Ngũ Hành Cục**: Thủy Nhị Cục / Mộc Tam Cục / Kim Tứ Cục / Thổ Ngũ Cục / Hỏa Lục Cục
2. **Cung Mệnh** (địa chi) + **Cung Thân** (địa chi) — hai cung này có thể đồng cung (Tý, Ngọ)
3. **Mệnh Chủ** (sao chủ cung Mệnh theo Ngũ Hành Cục)
4. **Thân Chủ** (sao chủ cung Thân theo giờ sinh)
5. **Tiên Thiên Bàn**: sắp xếp 12 cung theo thứ tự Tý→Sửu→Dần...→Hợi ngược kim đồng hồ

Output: Bảng tóm tắt nền tảng.

---

### BƯỚC 2 — Phân Tích Cung Mệnh + Cung Thân (Ưu Tiên Cao Nhất)

**Đọc từ `TV34_TuViNamPhai_Full.md` phần `### I. CUNG MỆNH, CUNG THÂN`**

Phân tích **cung Mệnh** (bản chất con người — phần cứng):
- Chính tinh tại cung Mệnh: tính cách cơ bản, ưu/nhược điểm
- Cát tinh / Sát tinh đi kèm: điều chỉnh tính cách tốt/xấu
- Tứ Hóa nhập Mệnh: Hóa Lộc/Quyền/Khoa → cát; Hóa Kị → trở lực
- Vượng độ của chính tinh (Miếu / Vượng / Đắc địa / Bình / Lạc hãm)
- Trạng thái Tràng Sinh của cung Mệnh

Phân tích **cung Thân** (tinh thần bên trong — phần mềm):
- Thân cư cung nào trong 12 cung → ảnh hưởng lĩnh vực đó suốt đời
- 3 tác dụng của cung Thân: Sửa đổi / Tăng cường / So sánh (trước 40 tuổi vs sau 40 tuổi)
- Quan hệ giữa Mệnh và Thân: cùng tốt / Mệnh tốt Thân yếu / Mệnh yếu Thân tốt

**Phán đoán tổng quan**: Mệnh mạnh hay yếu? Xu hướng trước thịnh sau suy hay ngược lại?

---

### BƯỚC 3 — Phân Tích Tam Phương Tứ Chính Cung Mệnh

**Tam Phương của cung Mệnh = Mệnh + Tài Bạch + Quan Lộc + Thiên Di (4 cung chính)**

Theo thứ tự quan trọng (từ `TV34_TuViNamPhai_Full.md` Chương V §1.1):
1. **Cung Mệnh** — đã phân tích ở bước 2
2. **Cung Phúc Đức** — nền tảng phúc khí, tinh thần, tâm linh
3. **Cung Thiên Di** (đối cung Mệnh) — cơ hội bên ngoài, xuất ngoại, thị phi
4. **Cung Tài Bạch** — tiền bạc, cách kiếm tiền, tài vận
5. **Cung Quan Lộc** — sự nghiệp, địa vị, nghề nghiệp

Với mỗi cung: liệt kê sao → tra nghĩa → nhận xét ngắn gọn (2–4 câu).

---

### BƯỚC 4 — Phân Tích 12 Cung Còn Lại

**Đọc `TV34_TuViNamPhai_Full.md` phần `## Chương II: MƯỜI HAI CUNG`**

Phân tích ngắn gọn các cung:
- **Cung Phu Thê** (tình cảm, hôn nhân): sao chính + nhận xét
- **Cung Tử Nữ** (con cái, học trò, sáng tạo): sao chính + nhận xét
- **Cung Tật Ách** (sức khỏe, bệnh tật): sao chính + cảnh báo nếu có sát tinh
- **Cung Bộc Dịch/Giao Hữu** (bạn bè, nhân viên): sao chính + nhận xét
- **Cung Điền Trạch** (bất động sản, nhà cửa, gia đình gốc): sao chính
- **Cung Huynh Đệ** (anh chị em, đối tác): sao chính
- **Cung Phụ Mẫu** (cha mẹ, cấp trên, văn bằng): sao chính

Format mỗi cung: `**[Tên cung]** ([sao trong cung]): [2–3 câu nhận xét]`

---

### BƯỚC 5 — Nhận Dạng Cách Cục

**Đọc `TV34_TuViNamPhai_Full.md` phần `### 1. SAO TỬ VI` → `### 14. PHÁ QUÂN`**
(Mỗi sao có mục §4: "Các cách cục có liên quan")

Scan tổ hợp sao trong cung Mệnh + Tam Phương Tứ Chính để tìm:

**Cách cục tốt (Quý Cách / Phú Cách)**: VD:
- Bách Quan Triều Củng Cách (Tử Vi miếu + lục cát tinh + Lộc Mã)
- Tử Phủ Triều Viên Cách (Tử Vi + Thiên Phủ đều miếu vượng)
- Nhật Lệ Trung Thiên Cách (Thái Dương tại Ngọ nhập Mệnh, không sát tinh)
- Cơ Nguyệt Đồng Lương Cách (Thiên Cơ, Thái Âm, Thiên Đồng, Thiên Lương)
- Sát Phá Tham Cách, Vũ Khúc Sát Phá Cách, v.v.

**Cách cục xấu (Phá Cách / hung cách)**: VD:
- Tứ Sát Công Chiếu (4 hung tinh cùng vào Mệnh)
- Hóa Kị nhập Mệnh + chính tinh lạc hãm
- Thiên La Địa Võng (Thìn/Tuất)

Với mỗi cách cục tìm được: **tên cách + điều kiện đủ/thiếu + ý nghĩa thực tế**.

---

### BƯỚC 6 — Phân Tích Đại Hạn Hiện Tại + Lưu Niên 2026

**Đọc `TV34_TuViNamPhai_Full.md` phần `## Chương 4`**

**Đại Hạn**:
- Xác định cung Đại Hạn hiện tại (10 năm đang hành)
- Dùng cung Đại Hạn làm "cung Mệnh tạm thời" → phân tích tam phương
- Tứ Hóa kích hoạt bởi can cung Đại Hạn → tác động đến các cung nào
- Nhận xét tổng quan 10 năm hạn này

**Lưu Niên 2026 (Bính Ngọ)**:
- Can năm 2026 = Bính → kích hoạt: Liêm Trinh Hóa Lộc, Thiên Đồng Hóa Quyền, Thiên Cơ Hóa Khoa, Văn Xương Hóa Kị
- Cung Lưu Niên = cung nào trong lá số có địa chi Ngọ
- Phân tích: Lộc nhập cung nào? Kị nhập cung nào? Tác động ra sao?
- Dự đoán: sự nghiệp / tài lộc / tình cảm / sức khỏe trong năm 2026

---

### BƯỚC 7 — Suy Luận Tổng Hợp + Kết Luận

**Đọc `TV34_TuViNamPhai_Full.md` phần `## Chương 5`**

Tổng hợp tất cả 6 bước trên thành bức tranh toàn diện:

**7.1. Chân dung tổng quát**
- Tính cách cốt lõi (3–5 điểm mạnh + 2–3 điểm yếu cần chú ý)
- Phong cách sống, quan điểm giá trị

**7.2. Sự nghiệp & Tài lộc**
- Phù hợp ngành nghề nào (tra theo `references/career-stars.md` hoặc từ sách)
- Cách kiếm tiền tốt nhất (chủ động / thụ động / đầu tư)
- Thời điểm phát tài / cần cẩn thận tài chính

**7.3. Tình cảm & Hôn nhân**
- Xu hướng tình cảm (sớm hay muộn, tốt hay nhiều trắc trở)
- Đặc điểm người bạn đời phù hợp

**7.4. Sức khỏe**
- Cơ quan cần chú ý (dựa vào sao trong cung Tật Ách + ngũ hành)
- Giai đoạn cần theo dõi sức khỏe

**7.5. Vận hạn tóm tắt**
- Giai đoạn tốt nhất trong cuộc đời (dựa vào Đại Hạn cát)
- Giai đoạn cần cẩn thận (Đại Hạn hung)
- Năm 2026 cụ thể: cơ hội gì? Rủi ro gì?

**7.6. Lời khuyên hành động**
3–5 gợi ý cụ thể phù hợp với cách cục và vận hạn hiện tại.

---

## Output Format

```markdown
# PHÂN TÍCH LÁ SỐ TỬ VI
**[Tên/Nickname]** | Năm sinh: [Can Chi] | Giới tính: [Nam/Nữ]
Ngũ Hành Cục: [X] | Cung Mệnh: [địa chi] | Cung Thân: [địa chi]
Phân tích theo: Mệnh Lý Thiên Cơ — Tam Hợp Nam Phái

---

## I. NỀN TẢNG LÁ SỐ
[Bảng 12 cung + sao, Mệnh Chủ, Thân Chủ]

## II. CUNG MỆNH & CUNG THÂN
[Phân tích chuyên sâu cung Mệnh + Thân, vượng độ, nhận xét tổng quan]

## III. TAM PHƯƠNG TỨ CHÍNH
[Cung Phúc Đức / Thiên Di / Tài Bạch / Quan Lộc]

## IV. MƯỜI HAI CUNG CHI TIẾT
[Tóm tắt 7 cung còn lại]

## V. CÁCH CỤC
[Liệt kê cách cục nhận dạng được + ý nghĩa]

## VI. ĐẠI HẠN & LƯU NIÊN 2026
[Phân tích hạn + dự đoán năm 2026]

## VII. TỔNG KẾT & LỜI KHUYÊN
[Chân dung / Sự nghiệp / Tình cảm / Sức khỏe / Hành động]
```

---

## Nguyên tắc phân tích

1. **Luôn tra sách** — Với mỗi sao quan trọng, đọc section tương ứng trong `TV34_TuViNamPhai_Full.md` để có giải thích chính xác theo trường phái Tam Hợp Nam Phái, không suy diễn tự do.

2. **Ưu tiên phân tích theo thứ tự**: Mệnh → Thân → Tam Phương → Cách Cục → Thời Gian. Không nhảy lung tung.

3. **Cân bằng cát/hung** — Không chỉ nói toàn tốt hoặc toàn xấu. Mọi lá số đều có điểm mạnh và điểm cần chú ý.

4. **Thực tế hiện đại** — Khi giải thích cách cục cổ đại (VD: "làm quan võ"), chuyển sang nghĩa hiện đại (VD: "phù hợp ngành quản lý, luật pháp, kỹ thuật").

5. **Độ sâu theo vượng độ** — Chính tinh Miếu/Vượng → phân tích đầy đủ; Đắc địa/Bình → phân tích trung bình; Lạc hãm → nêu rõ hạn chế.

6. **Trả lời câu hỏi cụ thể** — Nếu user hỏi thêm về một cung/sao/vận hạn cụ thể, tra thêm từ sách và trả lời chuyên sâu.

---

## Ví dụ nhận dạng cách cục thường gặp

| Tổ hợp sao | Cách cục | Ý nghĩa |
|------------|----------|---------|
| Tử Vi miếu + Tả Phù + Hữu Bật tại Mệnh | Bách Quan Triều Củng | Quyền lực, lãnh đạo, nổi tiếng xã hội |
| Tử Vi + Thiên Phủ đều miếu vượng chiếu Mệnh | Tử Phủ Triều Viên | Phú quý vẹn toàn |
| Thái Dương tại Ngọ nhập Mệnh, không sát | Nhật Lệ Trung Thiên | Danh tiếng, địa vị cao |
| Cơ Lương tại Thiên Di, Đồng Âm tại Mệnh | Cơ Nguyệt Đồng Lương | Phù hợp công chức, văn hóa giáo dục |
| Vũ Khúc + Thất Sát tại Mệnh, không sát | Vũ Sát triêu viên | Tướng lĩnh, y tế, kỹ thuật chính xác |
| Thái Dương lạc hãm + Kình Dương tại Mệnh | Mã đầu đới kiếm | Phải nỗ lực rất nhiều, dễ hao tổn |
| Hóa Kị + chính tinh lạc hãm tại Mệnh | Phá cách | Nhiều trở lực trong lĩnh vực cung đó |
