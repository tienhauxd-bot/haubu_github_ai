# Clone_YT — YouTube Story Cloner (English · Navy SEAL)

Nhận 1 YouTube URL → tự động transcribe → thiết kế câu chuyện Navy SEAL mới hoàn toàn → viết 12 chapter tiếng Anh (humanized) + Bài học + Hook → xuất file `.txt` + prompts Midjourney.

---

## Yêu Cầu Hệ Thống

| Công cụ | Cách cài |
|---------|---------|
| `uv` / `uvx` | `pip install uv` |
| `yt-dlp` | Tự động qua `uvx yt-dlp` |
| `openai-whisper` | Tự động qua `uvx --from openai-whisper whisper` |
| `ffmpeg` | Tải tại [ffmpeg.org](https://ffmpeg.org/download.html) → thêm vào PATH |

---

## Trigger

Gõ một trong các cụm sau trong Claude Code:

```
clone yt <YouTube URL>
clone video <YouTube URL>
tạo story từ video <YouTube URL>
/Clone_YT
```

---

## Quy Trình 5 Bước

| Bước | Tên | Thời điểm chờ duyệt |
|------|-----|---------------------|
| 1 | Lấy Transcript | Sau khi xong → hỏi bạn |
| 2 | Thiết Kế Câu Chuyện | Sau khi xong → hỏi bạn |
| 3 | Viết 12 Chapter (humanized) | Sau khi hoàn thành tất cả → hỏi bạn |
| 4 | Final Clean | Sau khi xong → hỏi bạn |
| 5 | Prompts Midjourney | Tự động hoàn thành |

### Bước 1 — Lấy Transcript

Script tự động download video và transcribe bằng Whisper:

```bash
python Clone_YT/scripts/download_and_transcribe.py --url "<YouTube URL>" --model small
```

**Tham số `--model`:** `tiny` (nhanh, kém chính xác) · `base` · `small` · `medium` · `large` (chậm, chính xác nhất)

### Bước 2 — Thiết Kế Câu Chuyện

Claude đọc transcript và tạo:
- Nhân vật mới 100% (tên Mỹ thực tế, không tái sử dụng)
- Bối cảnh mới (thành phố/tiểu bang Mỹ thực tế)
- Nhân vật chính: **1 Navy SEAL + 1 German Shepherd**
- Tóm tắt 12 chapter với cliffhanger từng chapter
- Happy ending bắt buộc + 1 tuyến phụ

Xuất file: `workspace/content/Clone_YT-[slug]/sum.txt`

### Bước 3 — Viết Nội Dung (Humanized)

Claude viết **liên tục 12 chapter** (không dừng giữa chừng):

| Quy tắc | Chi tiết |
|---------|---------|
| Độ dài | ~1200 từ/chapter tiếng Anh |
| Ngôi kể | Ngôi thứ ba |
| Văn phong | Thơ ca, huyền thoại nhẹ — cân bằng cảm xúc và hài hước |
| Humanization | Câu ngắn xen dài · cảm xúc → hành động vật lý · chi tiết giác quan cụ thể |

Sau Chapter 12: viết **Bài Học** (~200 từ) + **Hook** tiếng Anh.

Sau mỗi chapter: chạy format để chuẩn hóa định dạng:

```bash
python Clone_YT/scripts/fix_sentences.py <slug>
```

### Bước 4 — Final Clean

Đọc lại toàn bộ, xóa sạch: placeholder, ngoặc vuông, ghi chú nội bộ, dòng trống thừa, ký tự đặc biệt không cần thiết.

### Bước 5 — Prompts Midjourney

Tham khảo [references/camera-lighting.md](references/camera-lighting.md):
- 1 prompt chân dung/nhân vật chính
- 10 prompts/chapter (tuyến tính theo diễn biến)
- Nhân vật thứ 2 luôn quay lưng camera
- Mô tả đầy đủ từng prompt (không dùng "same")

---

## Output Files

Tất cả file xuất vào: `workspace/content/Clone_YT-[slug]/`

| File | Nội dung |
|------|---------|
| `sum.txt` | Bảng nhân vật + tóm tắt 12 chapter (tiếng Việt) |
| `chap-01.txt` → `chap-11.txt` | Nội dung chapter (tiếng Anh) |
| `chap-12.txt` | Chapter 12 + `---` + Bài Học |
| `hook.txt` | Hook tiếng Anh |
| `prompts.txt` | Tất cả prompts Midjourney (1 prompt/dòng) |

**Định dạng bắt buộc** (trừ `sum.txt` và `prompts.txt`):
- Mỗi câu trên 1 dòng riêng
- Không có dòng trống giữa các câu

---

## Cấu Trúc Thư Mục

```
Clone_YT/
├── README.md                   ← File này
├── skill.md                    ← Instruction file cho Claude Code
├── references/
│   ├── story-principles.md     ← Nguyên tắc nhân vật & phong cách
│   └── camera-lighting.md      ← Góc máy & ánh sáng cho Midjourney
└── scripts/
    ├── download_and_transcribe.py   ← Download YouTube + transcribe Whisper
    └── fix_sentences.py             ← Format: 1 câu/dòng, không dòng trống
```

---

## Nhân Vật Chính

### Navy SEAL
- Tuổi 28–45, có vết thương tâm lý (PTSD, mất người thân trong nhiệm vụ)
- Tên Mỹ thực tế: Marcus, Cole, Ryan, Derek, Nathan, Logan...
- Hành trình: học cách tin tưởng và yêu thương lại qua con chó

### German Shepherd
- Nhân vật quan trọng, không phải phụ kiện
- Mô tả màu lông cụ thể (sable, tan-black bicolor, solid black...)
- Tên: Rex, Titan, Duke, Ranger, Scout, Blaze...

---

## Khán Giả Mục Tiêu

Phụ nữ Mỹ 65+, nền tảng Thiên Chúa giáo, thích chia sẻ nội dung ấm lòng.
