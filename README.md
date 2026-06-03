# haubu_github_ai

Bộ **Skill & Agent** dành cho [Claude Code](https://claude.ai/code) — tập trung vào **Marketing AI** và **Tử Vi Nam Phái**.

---

## Cấu trúc repo

```
haubu_github_ai/
└── mkt/                          ← Thư mục chính (copy vào project của bạn)
    ├── CLAUDE.md                 ← Hướng dẫn cho Claude Code
    ├── BRANDVOICE.MD             ← Brand voice & tone
    ├── .claude/
    │   ├── agents/               ← Agent pipeline tự động
    │   └── skills/               ← Các skill độc lập
    └── README.md                 ← (file này)
```

---

## Danh sách Skills

### YouTube Story Cloner

| Skill | Ngôn ngữ output | Nhân vật chính | Chapter | Trigger |
|-------|----------------|----------------|---------|---------|
| [Clone_YT](Clone_YT/) | Tiếng Anh | Navy SEAL + Chó GSD | 12 chap + Bài học + Prompts MJ | `clone yt`, `clone video`, `/Clone_YT` |
| [Clone_YT_Nga](Clone_YT_Nga/) | Tiếng Nga | Cựu binh Liên Xô + Chó sói xám | Hook + 10 chap + Bài học + Prompts MJ | `clone nga`, `clone video nga`, `/Clone_YT_Nga` |

> Nhận 1 YouTube URL → tự động lấy transcript → thiết kế câu chuyện hoàn toàn mới → viết toàn bộ nội dung humanized → xuất file .txt + prompts Midjourney.

### Tử Vi & Mệnh Lý

| Skill | Mô tả | Trigger |
|-------|--------|---------|
| [tuvi-destiny-analyzer](mkt/.claude/skills/tuvi-destiny-analyzer/) | Phân tích lá số Tử Vi chuyên sâu theo **Tam Hợp Nam Phái** — 7 bước suy luận, nhận dạng cách cục, đại hạn & lưu niên | `phân tích lá số`, `xem tử vi`, `/tuvi-destiny-analyzer` |

### Marketing & Content

| Skill | Mô tả |
|-------|--------|
| breakout-video-finder | Tìm video viral theo chủ đề |
| github-trend-finder | Tìm trend GitHub cho nội dung tech |
| image-post-creator | Tạo post kèm ảnh |
| mkt-kane-* (nhiều skill) | Bộ skill theo phương pháp Brendan Kane (Hook Point, Going Viral) |
| mkt-create-script-* | Viết script video ngắn tiếng Việt |
| mkt-video-url-to-transcript | Chuyển video YouTube thành transcript |

> Xem đầy đủ tại [`mkt/.claude/skills/`](mkt/.claude/skills/)

---

## Cách dùng

### 1. Copy vào project của bạn

```bash
# Clone repo này
git clone https://github.com/tienhauxd-bot/haubu_github_ai.git

# Copy thư mục mkt vào project của bạn
cp -r haubu_github_ai/mkt/.claude /your-project/
```

### 2. Dùng với Claude Code

Mở Claude Code trong thư mục project, gõ trigger phrase hoặc slash command:

```
# Phân tích lá số Tử Vi
/tuvi-destiny-analyzer

# Tạo script video ngắn
/mkt-create-script-short-video-v2-vn

# Tìm trend viral
/mkt-kane-viral-format-identifier
```

### 3. Phân tích lá số Tử Vi

Skill `tuvi-destiny-analyzer` nhận 3 loại input:

**Cách A — Upload ảnh lá số:**
Đính kèm ảnh lá số trực tiếp trong chat.

**Cách B — Mô tả text:**
```
Năm sinh: Bính Dần (1986)
Giới tính: Nam
Ngũ Hành Cục: Mộc Tam Cục
Cung Mệnh: Hợi
Đại Hạn hiện tại: Hạn Dần (33-42)
Bố trí 12 cung: Tý: ..., Sửu: ..., Dần: ...
```

**Cách C — Ngày giờ sinh:**
```
Ngày sinh: 28/6/1986 (âm lịch)
Giờ sinh: Mùi (13:00-15:00)
Giới tính: Nam
```

Output: Phân tích markdown đầy đủ hoặc xuất PDF chất lượng cao.

---

## Agent Pipeline

**`mkt-brendan-kane-pipeline`** — Pipeline 9 bước tự động hóa toàn bộ quy trình tạo content viral:

```
GSB Research → Format ID → EOV [GATE 1]
→ Generalist Repackage → Platform Select [GATE 2]
→ Draft → Anti-pattern Audit (loop nếu có lỗi)
→ Triple F Boost + CTA Rewrite → Gold Review [GATE 3]
→ FINAL.md
```

---

## Yêu cầu

- [Claude Code](https://claude.ai/code) (CLI hoặc VSCode extension)
- Python 3.x (cho một số skill tạo ảnh/PDF)
- File `TV34_TuViNamPhai_Full.md` trong thư mục project (cho skill Tử Vi — không có trong repo vì dung lượng lớn)

---

## Đóng góp

Pull request và issue luôn được chào đón.

---

*Built with [Claude Code](https://claude.ai/code) · Powered by Anthropic*
