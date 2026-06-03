# Clone_YT_Nga — YouTube Story Cloner (Russian · Cựu Binh Liên Xô)

Nhận 1 YouTube URL → tự động transcribe → thiết kế câu chuyện cựu binh Liên Xô mới hoàn toàn → viết Hook + 10 chapter tiếng Nga (humanized) + Bài học → xuất 13 file `.txt` riêng biệt + prompts Midjourney.

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
clone nga <YouTube URL>
clone video nga <YouTube URL>
tạo story nga từ video <YouTube URL>
/Clone_YT_Nga
```

---

## Quy Trình 4 Bước

| Bước | Tên | Thời điểm chờ duyệt |
|------|-----|---------------------|
| 1 | Lấy Transcript | Sau khi xong → hỏi bạn |
| 2 | Thiết Kế Câu Chuyện | Sau khi xong → hỏi bạn |
| 3 | Viết Hook + 10 Chapter + Bài học (humanized) | Sau khi hoàn thành tất cả → hỏi bạn |
| 4 | Prompts Midjourney | Tự động hoàn thành |

### Bước 1 — Lấy Transcript

Script tự động download video và transcribe bằng Whisper:

```bash
python Clone_YT_Nga/scripts/download_and_transcribe.py --url "<YouTube URL>" --model small
```

**Tham số `--model`:** `tiny` (nhanh, kém chính xác) · `base` · `small` · `medium` · `large` (chậm, chính xác nhất)

### Bước 2 — Thiết Kế Câu Chuyện

Claude đọc transcript và tạo:
- Nhân vật mới 100% (tên Liên Xô/Nga thực tế, không tái sử dụng)
- Bối cảnh mới (địa danh Liên Xô/Nga thực tế)
- Nhân vật chính: **1 cựu binh Liên Xô ~50 tuổi + 1 chó sói màu xám**
- Không sử dụng nhân vật dưới 18 tuổi
- Tóm tắt 10 chapter với cliffhanger từng chapter
- Happy ending bắt buộc + 1 tuyến phụ (~20-30% dung lượng)

Xuất file: `workspace/content/Clone_YT_Nga-[slug]/Sum.txt`

### Bước 3 — Viết Nội Dung (Humanized)

Claude viết **liên tục toàn bộ** (Hook + 10 chapter + Bài học, không dừng giữa chừng):

| Quy tắc | Chi tiết |
|---------|---------|
| Độ dài | ~1100 từ/chapter tiếng Nga |
| Ngôi kể | Ngôi thứ ba |
| Chap 1 | Mở đầu bằng 1 câu thời tiết + thành phố |
| Chap 2+ | Đi thẳng vào nội dung, không mở đầu dài dòng |
| Ngôn ngữ | Tiếng Nga |
| Humanization | Câu ngắn xen dài · cảm xúc → phản ứng thể chất · chi tiết giác quan |
| Định dạng | Không cách dòng — toàn bộ nội dung liền mạch |

**Chap 0 (Hook):** Dựa trên style của video gốc (~1 phút đầu), viết lại cho câu chuyện mới bằng tiếng Nga.

**Chap 11 (Bài Học):** ~200 từ tiếng Nga, liên hệ đức tin/ơn Chúa tự nhiên, CTA kêu gọi "Amen", giọng ấm áp chân thành. Tuyệt đối không dùng ký tự đặc biệt (`*` `#` `—` `…`).

### Bước 4 — Prompts Midjourney

Tham khảo [references/camera-lighting.md](references/camera-lighting.md):
- 1 prompt chân dung/nhân vật (trang phục EMR, không logo)
- 10 prompts/chapter (Chap 1–10) + Hook
- Tuyết bám dày ở ngoài trời, không có tuyết trong nhà
- Không dùng `"same"` hay `"the same"` — mô tả đầy đủ từng prompt
- Nhân vật thứ 2 là người: `"a figure standing with their back to the camera"`
- Tất cả nhân vật: 100% người Nga/Liên Xô

---

## Output Files

Tất cả file xuất vào: `workspace/content/Clone_YT_Nga-[slug]/`

| File | Nội dung |
|------|---------|
| `Sum.txt` | Bảng nhân vật + tóm tắt 10 chapter (tiếng Việt) |
| `Chap-0.txt` | Hook (tiếng Nga) |
| `Chap-1.txt` → `Chap-10.txt` | Nội dung từng chapter (tiếng Nga) |
| `Chap-11.txt` | Bài học kết truyện (tiếng Nga) |
| `prompts.txt` | Tất cả prompts Midjourney (1 prompt/dòng, không số thứ tự) |

**Định dạng bắt buộc** (tất cả file Chap):
- Bắt đầu bằng tên chapter tiếng Nga (ví dụ: `Глава 1`), xuống dòng, nội dung ngay
- Không cách dòng — toàn bộ nội dung liền mạch
- Không ngoặc đơn, không ghi chú tên nhân vật trong đoạn văn

---

## Cấu Trúc Thư Mục

```
Clone_YT_Nga/
├── README.md                   ← File này
├── skill.md                    ← Instruction file cho Claude Code
├── references/
│   ├── story-principles.md     ← Nguyên tắc nhân vật & phong cách (Nga)
│   └── camera-lighting.md      ← Góc máy & ánh sáng cho Midjourney
└── scripts/
    ├── download_and_transcribe.py   ← Download YouTube + transcribe Whisper
    └── fix_sentences.py             ← Format file txt
```

---

## Nhân Vật Chính

### Cựu Binh Liên Xô
- ~50 tuổi, dày dạn trận mạc
- Tên Liên Xô/Nga thực tế: Aleksei, Dmitri, Viktor, Ivan, Nikolai...
- Trang phục đặc trưng: bộ đồ EMR (rừng số Nga), không logo

### Chó Sói Xám
- Nhân vật quan trọng trong câu chuyện
- Màu lông: xám rõ ràng trong mọi prompt Midjourney
- Thể hiện sự trung thành và bản năng hoang dã

---

## So Sánh Với Clone_YT

| | Clone_YT | Clone_YT_Nga |
|-|----------|-------------|
| Ngôn ngữ output | Tiếng Anh | Tiếng Nga |
| Nhân vật chính | Navy SEAL Mỹ | Cựu binh Liên Xô |
| Con vật | German Shepherd | Chó sói xám |
| Bối cảnh | Thành phố/tiểu bang Mỹ | Địa danh Liên Xô/Nga, có tuyết |
| Số chapter | 12 | 10 + Hook (Chap 0) + Bài học (Chap 11) |
| Định dạng file | 1 câu/dòng, không dòng trống | Liền mạch, không cách dòng |
| Khán giả | Phụ nữ Mỹ 65+, Thiên Chúa giáo | Người Nga yêu chuộng truyện đức tin |
