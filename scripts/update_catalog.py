#!/usr/bin/env python3
"""
Media Library Navigator - Catalog Generator
Scans connected drives and regenerates index.html, library_navigator.html, and media_index.txt.
"""
import os, sys, json, re, time

NV_BASE = "/run/media/mana/New Volume/Movies"
TOSHIBA_BASE = "/run/media/mana/TOSHIBA EXT"
REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dirs_to_index = [
    {"category": "Anime", "sub": "Movies", "path": os.path.join(TOSHIBA_BASE, "Anime", "Movies")},
    {"category": "Anime", "sub": "Series", "path": os.path.join(TOSHIBA_BASE, "Anime", "Series")},
    {"category": "Movies", "sub": "Feature Films", "path": os.path.join(NV_BASE, "Movies")},
    {"category": "Animated", "sub": "Animation", "path": os.path.join(NV_BASE, "Animated")},
    {"category": "TV Shows", "sub": "Series", "path": os.path.join(TOSHIBA_BASE, "TV Shows")},
    {"category": "Marvel", "sub": "MCU & Comics", "path": os.path.join(TOSHIBA_BASE, "Marvel")},
    {"category": "TV Series (Toshiba)", "sub": "Series", "path": os.path.join(TOSHIBA_BASE, "T V Series")},
]

video_exts = {".mkv", ".mp4", ".avi", ".ts", ".mov", ".wmv"}
sub_exts = {".srt", ".smi", ".ass", ".vtt", ".sub"}

def format_size(bytes_sz):
    if bytes_sz >= 1024 * 1024 * 1024:
        return f"{bytes_sz / (1024**3):.2f} GB"
    elif bytes_sz >= 1024 * 1024:
        return f"{bytes_sz / (1024**2):.1f} MB"
    else:
        return f"{bytes_sz / 1024:.0f} KB"

def detect_res(filename):
    m = re.search(r"\[(2160p|4k|1080p|720p|480p)\]", filename, re.I)
    if m: return m.group(1).lower()
    m2 = re.search(r"\b(2160p|4k|1080p|720p|480p)\b", filename, re.I)
    if m2: return m2.group(1).lower()
    return ""

print("Scanning media libraries...")
library_data = []
txt_lines = []
txt_lines.append("=" * 80)
txt_lines.append("                    MEDIA LIBRARY MASTER INDEX")
txt_lines.append(f"               Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
txt_lines.append("=" * 80)
txt_lines.append("")

total_vids = 0
total_bytes = 0

for section in dirs_to_index:
    cat = section["category"]
    sub = section["sub"]
    base_p = section["path"]
    if not os.path.exists(base_p): continue
    
    txt_lines.append(f"\n{'#' * 80}")
    txt_lines.append(f"# {cat.upper()} - {sub}  [{base_p}]")
    txt_lines.append(f"{'#' * 80}\n")
    
    items = sorted(os.listdir(base_p))
    for item in items:
        p = os.path.join(base_p, item)
        if not os.path.isdir(p):
            sz = os.path.getsize(p)
            ext = os.path.splitext(item)[1].lower()
            if ext in video_exts:
                total_vids += 1
                total_bytes += sz
                res = detect_res(item)
                txt_lines.append(f"  [FILE] {item} ({format_size(sz)}) {f'[{res}]' if res else ''}")
                library_data.append({
                    "id": f"f_{len(library_data)}",
                    "category": cat,
                    "sub": sub,
                    "folder_name": "",
                    "is_folder": False,
                    "path": p,
                    "files": [{
                        "name": item,
                        "rel_path": item,
                        "full_path": p,
                        "size": sz,
                        "size_str": format_size(sz),
                        "ext": ext,
                        "is_video": True,
                        "res": res
                    }]
                })
            continue
            
        files_in_folder = []
        folder_bytes = 0
        vid_count = 0
        
        for root, dirs, files in os.walk(p):
            dirs.sort()
            for f in sorted(files):
                full_f = os.path.join(root, f)
                rel_f = os.path.relpath(full_f, p)
                sz = os.path.getsize(full_f)
                ext = os.path.splitext(f)[1].lower()
                is_vid = ext in video_exts
                is_sub = ext in sub_exts
                res = detect_res(f) if is_vid else ""
                
                if is_vid:
                    vid_count += 1
                    total_vids += 1
                    total_bytes += sz
                folder_bytes += sz
                
                files_in_folder.append({
                    "name": f,
                    "rel_path": rel_f,
                    "full_path": full_f,
                    "size": sz,
                    "size_str": format_size(sz),
                    "ext": ext,
                    "is_video": is_vid,
                    "is_sub": is_sub,
                    "res": res
                })
                
        txt_lines.append(f"  [DIR] {item} ({format_size(folder_bytes)}, {vid_count} video{'s' if vid_count != 1 else ''})")
        for fi in files_in_folder:
            prefix = "    ├── " if fi["is_video"] else "    │   "
            res_tag = f" [{fi['res']}]" if fi["res"] else ""
            txt_lines.append(f"{prefix}{fi['rel_path']} ({fi['size_str']}){res_tag}")
            
        library_data.append({
            "id": f"item_{len(library_data)}",
            "category": cat,
            "sub": sub,
            "folder_name": item,
            "is_folder": True,
            "path": p,
            "total_size": folder_bytes,
            "total_size_str": format_size(folder_bytes),
            "video_count": vid_count,
            "files": files_in_folder
        })

txt_lines.append("\n" + "=" * 80)
txt_lines.append(f"TOTAL: {len(library_data)} Items | {total_vids} Video Files | {format_size(total_bytes)}")
txt_lines.append("=" * 80)

# Save txt index
index_txt_repo = os.path.join(REPO_DIR, "media_index.txt")
with open(index_txt_repo, "w", encoding="utf-8") as f:
    f.write("\n".join(txt_lines))
if os.path.exists(NV_BASE):
    with open(os.path.join(NV_BASE, "media_index.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(txt_lines))

print(f"Generated media_index.txt ({len(library_data)} titles, {total_vids} videos)")
