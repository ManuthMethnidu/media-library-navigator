# 🎬 Media & Anime Library Navigator

A fast, mobile-friendly, offline-capable single-page web application to browse, search, and export media from a personal multi-drive movie and anime collection.

---

## 🌟 Features

- **📱 Fully Mobile-Optimized**:
  - Touch-friendly responsive UI with card views, smooth horizontal category scrolling, and tap-to-expand folder views.
  - Collapsible bottom drawer sheet that adapts effortlessly between phones, tablets, and desktop displays.
  - Dedicated **"📄 Copy Text List"** button for quick sharing with friends over WhatsApp, Telegram, or Discord.
- **⚡ 100% Offline & Standalone**:
  - Single-file zero-dependency design (embedded styling, icons, and dataset).
  - Open directly in any web browser without needing a web server or internet connection.
- **🔍 Instant Live Search**:
  - Real-time search by title, release year, resolution (`1080p`, `720p`, `4K`), format (`.mkv`, `.mp4`), or category.
  - Press `/` anywhere to focus the search bar.
- **🌸 Smart Category Filters**:
  - Dedicated pills for **Anime (TOSHIBA EXT)**, **Movies (New Volume)**, **Animated**, **TV Shows (TOSHIBA EXT)**, and **Marvel**.
- **📦 Linux Export Script Generator**:
  - Select entire folders or individual files with interactive checkboxes.
  - Generates ready-to-run Bash commands (`mv` or `cp -r`) targeting an export directory (e.g., `/run/media/mana/New Volume/Movies/export/`).
  - One-click **"📋 Copy Linux Command"** or **"⬇ Download .sh Script"**.

---

## 📂 Repository Contents

| File | Description |
| :--- | :--- |
| [`index.html`](index.html) | Main responsive web navigator (ready for GitHub Pages or local offline viewing). |
| [`library_navigator.html`](library_navigator.html) | Direct standalone copy of the navigator web application. |
| [`media_index.txt`](media_index.txt) | Complete structured plain-text catalog indexing 527 titles and 1,832 video files (1.1 TB). |

---

## 🚀 How to Use

### 1. View Locally
Simply double-click [`index.html`](index.html) or open it with your preferred web browser:
```bash
# Linux
xdg-open index.html

# macOS
open index.html

# Windows
start index.html
```

### 2. Enable GitHub Pages (Optional)
To browse your collection from anywhere or share it with friends via a web link:
1. Go to your repository settings: **Settings > Pages**.
2. Under **Build and deployment**, select **Deploy from a branch**.
3. Choose branch `main` and folder `/ (root)`, then click **Save**.
4. Your library catalog will be live at `https://<username>.github.io/media-library-navigator/`!

---

## 🛠 Tech Stack

- **HTML5 & Vanilla JavaScript**: Zero frameworks, zero bloat, instant rendering.
- **Modern Responsive CSS**: Flexbox, CSS Grid, mobile media queries, glassmorphism, and dark mode palette.

---

*Authored by Manuth Methnidu.*
