---
name: Clone_YT
description: >
  Nhận 1 YouTube URL → clone thành câu chuyện Navy SEAL mới hoàn toàn → 12 chapter tiếng Anh
  (~1200 từ/chap, viết thẳng bản humanized) + Bài học + Hook → Final Clean → xuất file .txt + prompts Midjourney.
  USE WHEN user nói "clone yt", "clone video", "tạo story từ video", "Clone_YT",
  hoặc dán link YouTube và muốn clone thành câu chuyện SEAL mới.
---

# Clone_YT — YouTube Story Cloner

## References
- [Nguyên tắc phong cách & nhân vật](references/story-principles.md) — đọc trước Bước 2
- [Góc máy & ánh sáng Midjourney](references/camera-lighting.md) — đọc trước Bước 5

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
| 4 | Final Clean | Sau khi xong |
| 5 | Prompts Midjourney | — |

## Output Directory

Tất cả file xuất vào: `workspace/content/Clone_YT-[story-slug]/`

| File | Nội dung |
|------|---------|
| `sum.txt` | Bảng nhân vật + tóm tắt 12 chapter (tiếng Việt) |
| `chap-01.txt` → `chap-12.txt` | Nội dung từng chapter (tiếng Anh) |
| `chap-12.txt` | Chapter 12 + Bài Học ở cuối |
| `hook.txt` | Hook tiếng Anh |
| `prompts.txt` | Tất cả prompts Midjourney |

## Định Dạng File Bắt Buộc

**Tất cả file .txt** (trừ `sum.txt` và `prompts.txt`) phải tuân theo định dạng:
- **Mỗi câu trên 1 dòng riêng**
- **Không có dòng trống** giữa các câu
- Ngoại lệ duy nhất: dấu `---` phân cách story và Bài Học trong `chap-12.txt`

Sau khi viết xong mỗi file, chạy script format để chuẩn hóa:

```bash
python .claude/skills/Clone_YT/scripts/fix_sentences.py <slug>
```

Hoặc áp dụng thủ công khi dùng Write tool: viết nội dung đã tách câu sẵn, không dùng dòng trống.

---

## Bước 1 — Lấy Transcript

```bash
python .claude/skills/Clone_YT/scripts/download_and_transcribe.py \
  --url "<URL>" --model small
```

Phân tích transcript, trích xuất: cốt truyện, nhân vật gốc, bối cảnh, hook gốc, tình tiết chính.

> Nếu không download được: báo lỗi, dừng.

**→ Hiển thị kết quả. Hỏi: "Bước 1 xong. Tiếp Bước 2?"**

---

## Bước 2 — Thiết Kế Câu Chuyện Mới

**Yêu cầu:**
- Tên nhân vật: 100% tên Mỹ thực tế, tên mới mỗi lần (không tái sử dụng)
- Địa danh: thành phố/tiểu bang Mỹ thực tế, mới mỗi lần
- Nhân vật chính: 1 Navy SEAL + 1 German Shepherd
- Giữ tình tiết gốc, đổi hoàn toàn bối cảnh và tên
- Happy ending bắt buộc + 1 tuyến phụ
- Kiểm tra logic trước khi tiếp tục

**Output (tiếng Việt):**

```
NHÂN VẬT CHÍNH: Tên / Tuổi / Ngoại hình / Tính cách / Trang phục / Hoàn cảnh đặc biệt
CHÓ GSD: Tên / Tuổi / Màu lông / Đặc điểm / Tính cách
NHÂN VẬT PHỤ: Tên / Vai trò / Mô tả ngắn
```

Tóm tắt 12 chapter (5-8 dòng/chap), có cliffhanger mỗi chapter, chapter 12 là happy ending.

Xuất file: `workspace/content/Clone_YT-[slug]/sum.txt`

**→ Hỏi: "Bước 2 xong. Tiếp Bước 3 — viết Chapter 1?"**

---

## Bước 3 — Triển Khai Nội Dung (đã humanized)

Viết **tất cả 12 chapter liên tục**, không dừng hỏi giữa các chapter. Chỉ dừng sau khi toàn bộ Bước 3 (12 chapter + Bài Học + Hook) hoàn thành.

**Viết thẳng bản final — không viết draft rồi rewrite lại.**

**Quy tắc nội dung:**

| Quy tắc | Chi tiết |
|---------|---------|
| Độ dài | ~1200 từ tiếng Anh |
| Ngôi kể | Ngôi thứ ba |
| Nhân vật mới | Mô tả đầy đủ lần đầu xuất hiện; tuổi chỉ nhắc 1 lần |
| Không ngoặc đơn | Không chú thích trong đoạn |
| Đầu chapter | 1-2 câu thời tiết + địa điểm |
| Cuối chapter | Cliffhanger (trừ Chap 12) |
| Chia đoạn | Mỗi đoạn 1 tình tiết/cảnh |
| Văn phong | Tiếng Anh, thơ ca/huyền thoại nhẹ, cân bằng cảm xúc và hài hước |

**Quy tắc humanization — áp dụng ngay khi viết, không viết draft rồi rewrite:**
- **Câu ngắn đột ngột** xen giữa câu dài — tạo nhịp thở tự nhiên
- **Không dùng:** "First / Second / Finally", "It is worth noting", "It goes without saying", câu liệt kê ba vế đối xứng hoàn hảo
- **Cảm xúc → hành động vật lý:** thay "he felt afraid" bằng "his hands were shaking — not from cold"
- **Chi tiết giác quan cụ thể:** mùi, nhiệt độ, tiếng động, kết cấu bề mặt
- **Đa dạng độ dài câu:** xen lẫn câu 1-3 từ, câu trung bình, câu dài — không đều nhau

Sau mỗi chapter: xuất `chap-0N.txt` theo đúng định dạng (mỗi câu 1 dòng, không dòng trống) + report ngắn (thay đổi so với tóm tắt + tóm tắt 3-5 câu tiếng Việt). Sau đó **tiếp tục ngay Chapter tiếp theo** mà không hỏi.

Sau Chapter 12:
- Viết **Bài Học** ~200 từ tiếng Anh → dán cuối `chap-12.txt` (sau dấu `---`)
- Viết **Hook** tiếng Anh → xuất `hook.txt`

**→ Sau khi Hook xong, hỏi: "Bước 3 xong. Tiếp Bước 4 — Final Clean?"**

---

## Bước 4 — Final Clean

Đọc lại toàn bộ các file .txt và xóa sạch:
- Mọi dấu ngoặc vuông `[...]` còn sót lại
- Mọi placeholder chưa được điền
- Mọi ghi chú nội bộ, comment, hoặc hướng dẫn lọt vào văn bản
- Dòng trống thừa giữa các đoạn
- Ký tự đặc biệt không cần thiết (*, #, —, … nếu không phải dấu câu tự nhiên)

Ghi đè lên từng file .txt sau khi clean xong.

**→ Hỏi: "Bước 4 xong. Tiếp Bước 5 — Prompts Midjourney?"**

---

## Bước 5 — Prompts Midjourney

**Đọc [references/camera-lighting.md](references/camera-lighting.md) trước khi viết prompts.**

**Chân dung nhân vật:** 1 prompt/nhân vật chính — chỉ mô tả vật lý (không ghi tên), cinematic portrait, photorealistic. Kèm bản dịch tiếng Việt ngoài code block.

**10 prompts/chapter + Hook:**

| Quy tắc | Chi tiết |
|---------|---------|
| Số lượng | 10 prompts/chapter |
| Tuyến tính | Theo thứ tự diễn biến chapter |
| Nhân vật | 1 nhân vật chính/prompt; người thứ 2 luôn quay lưng camera |
| Mô tả | Mô tả đầy đủ mỗi prompt (tuổi, trang phục, màu lông) — không dùng "same" |
| Góc & ánh sáng | Đa dạng, nhất quán theo thời gian trong ngày (xem reference) |
| Format | 100% tiếng Anh, 1 dòng/prompt; bản dịch tiếng Việt bên dưới |
| Cấm | Portrait close-up mặt đầy khung |

**File tổng hợp:** `workspace/content/Clone_YT-[slug]/prompts.txt` — tất cả prompts Chap 1–12 + Hook, 1 prompt/dòng, không tiêu đề.
