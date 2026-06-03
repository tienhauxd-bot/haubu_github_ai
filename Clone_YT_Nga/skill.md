---
name: Clone_YT_Nga
description: >
  Nhận 1 YouTube URL → clone thành câu chuyện cựu binh Liên Xô mới hoàn toàn → 10 chapter tiếng Nga
  (~1100 từ/chap, viết thẳng bản humanized) + Bài học (Chap 11) + Hook (Chap 0) → xuất 13 file txt riêng biệt (Sum + Chap-0 đến Chap-11, không cách dòng) + prompts.txt (Midjourney).
  USE WHEN user nói "clone nga", "clone video nga", "tạo story nga từ video", "Clone_YT_Nga",
  hoặc dán link YouTube và muốn clone thành câu chuyện cựu binh Liên Xô mới.
---

# Clone_YT_Nga — YouTube Story Cloner (Russian Edition)

## References
- [Nguyên tắc phong cách & nhân vật](references/story-principles.md) — đọc trước Bước 2
- [Góc máy & ánh sáng Midjourney](references/camera-lighting.md) — đọc trước Bước 4

## Scripts (tự-đủ — không cần cài skill khác)

| Script | Mục đích |
|--------|---------|
| `scripts/download_and_transcribe.py` | Download YouTube + transcribe bằng Whisper cục bộ |
| `scripts/fix_sentences.py` | Format mỗi câu trên 1 dòng, xóa dòng trống thừa |

**Yêu cầu hệ thống:**
- `uv` / `uvx`: cài bằng `pip install uv`
- `yt-dlp`: chạy tự động qua `uvx yt-dlp`
- `openai-whisper`: chạy tự động qua `uvx --from openai-whisper whisper`
- `ffmpeg`: cài từ https://ffmpeg.org/download.html (thêm vào PATH)

## Quy Trình

| Bước | Tên | Chờ duyệt |
|------|-----|-----------|
| 1 | Lấy Transcript | Sau khi xong |
| 2 | Thiết Kế Câu Chuyện | Sau khi xong |
| 3 | Triển Khai Nội Dung (đã humanized) | Sau khi hoàn thành toàn bộ Bước 3 |
| 4 | Prompts Midjourney | — |

## Output

**Story content:** Mỗi phần xuất vào **file txt riêng biệt** trong thư mục `workspace/content/Clone_YT_Nga-[story-slug]/`.

**Prompts:** Xuất vào file `workspace/content/Clone_YT_Nga-[story-slug]/prompts.txt`

| File | Nội dung |
|------|---------|
| `Sum.txt` | Bảng nhân vật + tóm tắt 10 chapter (tiếng Việt) |
| `Chap-0.txt` | Hook tiếng Nga |
| `Chap-1.txt` → `Chap-10.txt` | Nội dung từng chapter (tiếng Nga) |
| `Chap-11.txt` | Bài học kết truyện (tiếng Nga) |

**Quy tắc định dạng nội dung file txt:**
- **Không cách dòng** giữa các câu hoặc đoạn — toàn bộ nội dung liền mạch
- Bắt đầu bằng tên chapter (ví dụ: `Глава 1`), xuống dòng, rồi nội dung ngay
- Không có dòng trống thừa ở bất kỳ vị trí nào trong file

## Định Dạng Nội Dung Bắt Buộc

**Tất cả chapter tiếng Nga** phải tuân theo:
- Bắt đầu bằng tên chap (ví dụ: `Глава 1`), xuống dòng, rồi nội dung — **không cách dòng** giữa các câu hoặc đoạn
- Không có dòng trống ở bất kỳ vị trí nào trong file
- Không dùng ngoặc đơn trong đoạn văn
- Không chú thích tên nhân vật trong đoạn văn
- Không mô tả lại tuổi/ngoại hình nhân vật sau lần đầu giới thiệu

---

## Bước 1 — Lấy Transcript

```bash
python .claude/skills/Clone_YT_Nga/scripts/download_and_transcribe.py \
  --url "<URL>" --model small
```

Phân tích transcript, trích xuất: cốt truyện, nhân vật gốc, bối cảnh, hook gốc (khoảng 1 phút đầu), tình tiết chính.

> Nếu không download được: báo lỗi, dừng.

**→ Hiển thị kết quả. Hỏi: "Bước 1 xong. Tiếp Bước 2?"**

---

## Bước 2 — Thiết Kế Câu Chuyện Mới

**Đọc [references/story-principles.md](references/story-principles.md) trước khi làm bước này.**

**Yêu cầu:**
- Tình tiết tương tự video gốc, **happy ending bắt buộc**
- Đổi địa điểm → địa danh Liên Xô/Nga thực tế, mới mỗi lần
- Đổi tên → **100% tên người Liên Xô/Nga**, mới mỗi lần (không tái sử dụng)
- Nhân vật chính: **1 cựu binh Liên Xô ~50 tuổi + 1 chó sói màu xám**
- **Không sử dụng nhân vật dưới 18 tuổi**
- Phát triển thêm **1 tuyến phụ** song song tuyến chính (~20-30% dung lượng)
- Kiểm tra logic trước khi finalize
- Khoảng **10 chapter**

**Output (tiếng Việt):**

```
NHÂN VẬT CHÍNH: Tên / Tuổi / Ngoại hình / Tính cách / Trang phục / Hoàn cảnh đặc biệt
CHÓ SÓI: Tên / Tuổi ước tính / Màu lông / Đặc điểm / Tính cách
NHÂN VẬT PHỤ: Tên / Vai trò / Mô tả ngắn
```

Tóm tắt 10 chapter (5-8 dòng/chap), có cliffhanger mỗi chapter (trừ chap 10), chapter 10 là happy ending.

Kiểm tra tình tiết vô lý → sửa ngay, ghi chú rõ.

**→ Xuất vào file `workspace/content/Clone_YT_Nga-[slug]/Sum.txt`** (tạo thư mục nếu chưa có).

**→ Hỏi: "Bước 2 xong. Tiếp Bước 3 — viết Chapter 1?"**

---

## Bước 3 — Triển Khai Nội Dung (đã humanized)

Viết **tất cả chapter liên tục**, không dừng hỏi giữa các chapter. Chỉ dừng sau khi toàn bộ Bước 3 (10 chapter + Bài Học + Hook) hoàn thành.

**Viết thẳng bản final — không viết draft rồi rewrite lại.**

### Quy Tắc Nội Dung

| Quy tắc | Chi tiết |
|---------|---------|
| Độ dài | ~1100 từ tiếng Nga (Chap 1); các chap sau tương đương |
| Ngôi kể | Ngôi thứ ba |
| Nhân vật mới | Mô tả đầy đủ lần đầu xuất hiện: dáng vẻ, ngoại hình, tính cách, sự kiện ảnh hưởng tính cách (nếu có). Nhân vật chính mô tả chi tiết, nhân vật phụ mô tả đơn giản hơn. |
| Tuổi nhân vật | Chỉ nhắc 1 lần duy nhất khi giới thiệu — **không mô tả lại sau đó** |
| Không ngoặc đơn | Không chú thích trong đoạn văn |
| Bối cảnh Chap 1 | 1 câu mô tả thời tiết + thành phố ở đầu chapter |
| Chap 2 trở đi | Đi thẳng vào nội dung, không mở đầu dài dòng |
| Cuối chapter | Cliffhanger (trừ Chap 10) — kết trong nội dung tóm tắt |
| Ngôn ngữ | Tiếng Nga |
| Không thêm | Chỉ triển khai đúng đề cương chapter, không tự thêm tuyến sự kiện ngoài kế hoạch |
| Không lặp lại | Không lặp ý đã nói |
| Ưu tiên | Diễn biến, hành động, tiến triển cốt truyện |

### Quy Tắc Humanization — Áp dụng ngay khi viết

- **Câu ngắn đột ngột** xen giữa câu dài — tạo nhịp thở tự nhiên
- **Không dùng:** cấu trúc liệt kê ba vế đối xứng hoàn hảo, câu mở đầu sáo rỗng
- **Cảm xúc → hành động vật lý:** thay mô tả cảm xúc trực tiếp bằng phản ứng thể chất cụ thể
- **Chi tiết giác quan cụ thể:** mùi, nhiệt độ, tiếng động, kết cấu bề mặt
- **Đa dạng độ dài câu:** xen lẫn câu ngắn 1-3 từ, câu trung bình, câu dài — không đều nhau
- **Mô tả ngắn gọn, đủ hình dung** — không mô tả lan man, không giải thích thừa, không kéo dài tâm lý nhân vật

### Định Dạng Xuất

Sau mỗi chapter:
1. Xuất nội dung → file riêng `workspace/content/Clone_YT_Nga-[slug]/Chap-N.txt` (bắt đầu bằng tên chap tiếng Nga, xuống dòng, nội dung liền mạch, **không cách dòng**)
2. Báo cáo ngắn: thay đổi so với tóm tắt (nếu có) + tóm tắt 3-5 câu tiếng Việt
3. **Tiếp tục ngay chapter tiếp theo** — không hỏi

### Chap 11 — Bài Học Kết Truyện

Sau Chap 10, viết **Bài Học** (~200 từ tiếng Nga):
- Liên hệ đến phép màu / ơn Chúa / đức tin một cách tự nhiên, không giảng đạo
- Áp dụng vào cuộc sống hàng ngày
- Call to action: kêu gọi chia sẻ, comment, đăng ký kênh
- Kêu gọi comment **"Amen"** phù hợp với tinh thần câu chuyện
- Cầu Chúa phù hộ cho những người xem
- **Tuyệt đối không dùng ký tự đặc biệt:** không *, không #, không —, không …
- Giọng văn: ấm áp, chân thành

→ Xuất vào file `workspace/content/Clone_YT_Nga-[slug]/Chap-11.txt` (không cách dòng)

### Hook — Chap 0

Dựa trên style của video gốc (khoảng 1 phút đầu) để viết lại Hook cho câu chuyện của mình, bằng tiếng Nga, với nội dung kịch bản, nhân vật, bối cảnh là cốt truyện của mình.

→ Xuất vào file `workspace/content/Clone_YT_Nga-[slug]/Chap-0.txt` (không cách dòng)

**→ Sau khi Hook xong, hỏi: "Bước 3 xong. Tiếp Bước 4 — Prompts Midjourney?"**

---

## Bước 4 — Prompts Midjourney

**Đọc [references/camera-lighting.md](references/camera-lighting.md) trước khi viết prompts.**

### Chân Dung Nhân Vật

Liệt kê các nhân vật trong truyện. Với mỗi nhân vật, viết 1 prompt Midjourney mô tả chân dung, bao gồm:
- Ngoại hình chi tiết: tuổi, màu da, màu tóc, đặc điểm nhận dạng
- Trang phục nhân vật chính: bộ đồ **EMR (không có chữ, logo)**
- Màu lông động vật (chó sói phải rõ màu lông xám)
- Cinematic portrait, photorealistic
- **Không ghi tên nhân vật** trong prompt

Kèm bản dịch tiếng Việt ngoài code block.

### 10 Prompts / Chapter

Áp dụng cho tất cả Chap 1–10 và Hook:

| Quy tắc | Chi tiết |
|---------|---------|
| Số lượng | 10 prompts/chapter |
| Tuyến tính | Theo thứ tự diễn biến chapter |
| Prompt đầu tiên mỗi chap | Mô tả thời tiết/bối cảnh cảnh mở đầu |
| Nhân vật | Mô tả đầy đủ mỗi prompt (tuổi, trang phục, màu lông) — **không dùng "same" hay "the same"** |
| Góc & ánh sáng | Đa dạng theo tình tiết, nhất quán theo thời gian trong ngày |
| Thời gian trong ngày | Xem lại kỹ — đồng nhất tuyến tính, rõ ràng trong từng prompt |
| Format | 100% tiếng Anh, 1 dòng/prompt |
| Bên ngoài | Tuyết bám dày trên tất cả mọi thứ (ở ngoài trời) |
| Trong nhà | Không có tuyết |
| Cấm | Portrait close-up khuôn mặt chiếm toàn khung |
| Cấm | Ghi tên nhân vật trong prompt |
| Cấm | Số thứ tự trước mỗi prompt |
| Cấm | "same", "the same" |
| Nhân vật thứ 2 là người | "a figure standing with their back to the camera" |
| Tất cả nhân vật | 100% người Nga/Liên Xô |

**Bản dịch tiếng Việt** đặt bên ngoài code block (dưới mỗi đoạn code).

### File Tổng Hợp Prompts

Tất cả prompts Chap 1–10 + Hook → file `workspace/content/Clone_YT_Nga-[slug]/prompts.txt`:
- 1 prompt/dòng
- Không tiêu đề, không chú thích
- Không đánh số thứ tự

Sau khi viết xong, chạy format:

```bash
python .claude/skills/Clone_YT_Nga/scripts/fix_sentences.py <slug>
```
