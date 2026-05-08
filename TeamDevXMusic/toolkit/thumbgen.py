"""
                      [TeamDev](https://t.me/team_x_og)
          
          Project Id -> 39.
          Project Name -> TeamDev X Music
          Project Age -> 15D+ (Updated On 05/05/2026)
          Project Idea By -> @MR_ARMAN_08
          Project Dev -> @MR_ARMAN_08
          Powered By -> @Team_X_Og ( On Telegram )
          Updates -> @TeamDevXBots ( On telegram )
    
    Setup Guides -> Read > README.md
    
          This Script Part Off https://t.me/Team_X_Og's Team.
          Copyright ©️ 2026 TeamDev | @Team_X_Og
          
    • Some Quick Help
    - Read Full README.md For Understanding The Content.
    - If You Need Any Help Contact Us In @Team_X_Og's Group
    
         Compatible In BotApi 9.5 Fully
         Build For BotApi 9.5
         We'll Keep Update This Repo If We Got 30+ Stars In One Month Of Release.
"""

# Copyright (C) 2025 by @MR_ARMAN_08 @ Github, < https://github.com/justfortestingnothibghere >
# All rights reserved. © TeamDevXMusic

"""
TeamDevXMusic is a Telegram Music Bot by @MR_ARMAN_08.
Copyright (c) 2026 ~ Present Team TeamDevXMusic <https://github.com/justfortestingnothibghere>

This program is "Ristiricted" software: Don't Modify, Redistribute Or Sell This Project Proving As Your Project
TeamDev Will Take Action If They Find Any unauthorised usages.
"""

import io
import math
import os
import random
import re
import textwrap

import aiofiles
import aiohttp
from PIL import (
    Image, ImageDraw, ImageEnhance,
    ImageFilter, ImageFont, ImageOps
)
from youtubesearchpython.__future__ import VideosSearch

from config import YOUTUBE_IMG_URL

W, H = 1280, 720

ASSETS      = "assets"
F_BOLD      = os.path.join(ASSETS, "font2.ttf")
F_REG       = os.path.join(ASSETS, "font.ttf")

DARK    = (4,  11, 26)
BOX_BG  = (8,  20, 45)
BOX_BD  = (12, 40, 72)
CYAN    = (0,  212, 255)
CYAN_D  = (0,  120, 200)
WHITE   = (255, 255, 255)
GREY    = (150, 170, 195)

def _fnt(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def _glow_rect(canvas: Image.Image, xy, radius: int,
               color: tuple, blur: int = 8, alpha: int = 180) -> Image.Image:
    glow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    gd   = ImageDraw.Draw(glow)
    x0, y0, x1, y1 = xy
    for s in range(20, 0, -3):
        a = int(alpha * s / 20)
        gd.rounded_rectangle(
            [x0 - s, y0 - s, x1 + s, y1 + s],
            radius=radius + s,
            outline=(*color, a),
            width=3,
        )
    glow   = glow.filter(ImageFilter.GaussianBlur(blur))
    canvas = Image.alpha_composite(canvas.convert("RGBA"), glow)
    return canvas


def _rounded_paste(canvas: Image.Image, src: Image.Image,
                   xy: tuple, radius: int) -> None:
    src = src.convert("RGBA")
    mask = Image.new("L", src.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, src.width - 1, src.height - 1],
        radius=radius,
        fill=255,
    )
    canvas.paste(src, xy, mask)


def _waveform(draw: ImageDraw.ImageDraw, cx: int, cy: int,
              color: tuple, bars: int = 11) -> None:
    heights = [10, 16, 24, 32, 40, 48, 40, 32, 24, 16, 10]
    bw, gap = 5, 7
    tw = bars * bw + (bars - 1) * gap
    sx = cx - tw // 2
    for i, h in enumerate(heights[:bars]):
        bx = sx + i * (bw + gap)
        draw.rounded_rectangle(
            [bx, cy - h, bx + bw, cy + h],
            radius=2,
            fill=(*color, 220),
        )


def _circle_icon(draw: ImageDraw.ImageDraw, cx: int, cy: int,
                 r: int, color: tuple, kind: str) -> None:
    c = (*color, 230)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=c, width=2)
    if kind == "eye":
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=c)
        draw.arc([cx-r+3, cy-r//2+1, cx+r-3, cy+r//2-1], 200, 340, fill=c, width=2)
        draw.arc([cx-r+3, cy-r//2+1, cx+r-3, cy+r//2-1],  20, 160, fill=c, width=2)
    elif kind == "clock":
        draw.line([cx, cy - r + 5, cx, cy], fill=c, width=2)
        draw.line([cx, cy, cx + r - 5, cy], fill=c, width=2)
    elif kind == "person":
        draw.ellipse([cx - 5, cy - r + 3, cx + 5, cy - r // 2 + 5], fill=c)
        draw.arc([cx - r//2, cy - r//4, cx + r//2, cy + r//2], 0, 180, fill=c, width=2)
    elif kind == "bolt":
        pts = [(cx + 4, cy - r + 2), (cx - 3, cy + 2),
               (cx + 3, cy + 2),     (cx - 4, cy + r - 2)]
        draw.polygon(pts, fill=c)


def _scatter_particles(draw: ImageDraw.ImageDraw, seed: int = 7) -> None:
    random.seed(seed)
    for _ in range(38):
        px, py = random.randint(0, W), random.randint(0, H)
        pr     = random.randint(1, 4)
        pa     = random.randint(20, 90)
        col    = random.choice([CYAN, CYAN_D, WHITE])
        draw.ellipse([px - pr, py - pr, px + pr, py + pr], fill=(*col, pa))

def _build_thumbnail(
    cover_img: Image.Image,
    title: str,
    views: str,
    duration: str,
    owner: str,
) -> Image.Image:
    fnt_np    = _fnt(F_BOLD, 72)
    fnt_title = _fnt(F_BOLD, 46)
    fnt_info  = _fnt(F_BOLD, 34)
    fnt_brand = _fnt(F_REG,  27)

    canvas = Image.new("RGBA", (W, H), (*DARK, 255))
    grad   = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd     = ImageDraw.Draw(grad)
    for y in range(H):
        a = int(60 * (y / H) ** 1.5)
        gd.line([(0, y), (W, y)], fill=(0, 30, 60, a))
    canvas = Image.alpha_composite(canvas, grad)
    draw   = ImageDraw.Draw(canvas)

    _scatter_particles(draw)

    L0, L1, L2, L3 = 32, 28, 578, 692
    CARD_R = 30

    canvas = _glow_rect(canvas, (L0, L1, L2, L3), CARD_R, CYAN, blur=8, alpha=180)
    draw   = ImageDraw.Draw(canvas)
    draw.rounded_rectangle([L0, L1, L2, L3], radius=CARD_R,
                            fill=(*BOX_BG, 255), outline=(*CYAN, 230), width=3)

    pad = 28
    cw, ch = (L2 - L0) - 2 * pad, (L3 - L1) - 2 * pad
    cover_resized = cover_img.convert("RGBA").resize((cw, ch), Image.LANCZOS)
    _rounded_paste(canvas, cover_resized, (L0 + pad, L1 + pad), radius=18)
    draw = ImageDraw.Draw(canvas)

    RX = 615

    _waveform(draw, RX + 160, 70, CYAN)

    nw = draw.textlength("NOW ", font=fnt_np)
    draw.text((RX, 92),      "NOW ",    fill=WHITE, font=fnt_np)
    draw.text((RX + nw, 92), "PLAYING", fill=CYAN,  font=fnt_np)

    rows = [
        ("title",  None,    textwrap.shorten(title,    width=22, placeholder="…")),
        ("eye",    None,    views),
        ("clock",  None,    duration),
        ("person", None,    owner),
    ]
    icons = ["title", "eye", "clock", "person"]

    BY, BH, GAP = 228, 88, 11
    for i, (icon, _, val) in enumerate(rows):
        by0 = BY + i * (BH + GAP)
        by1 = by0 + BH
        bx0, bx1 = RX, W - 22
        cy = (by0 + by1) // 2

        draw.rounded_rectangle([bx0, by0, bx1, by1], radius=18,
                                fill=(*BOX_BG, 255), outline=(*BOX_BD, 255), width=2)

        if icon == "title":
            draw.text((bx0 + 22, cy), val, fill=WHITE, font=fnt_title, anchor="lm")
        else:
            _circle_icon(draw, bx0 + 42, cy, 18, CYAN, icon)
            draw.line([(bx0 + 76, by0 + 18), (bx0 + 76, by1 - 18)],
                      fill=(*CYAN_D, 140), width=1)
            draw.text((bx0 + 92, cy), val, fill=WHITE, font=fnt_info, anchor="lm")

    # Branding bar
    bb0 = BY + 4 * (BH + GAP) + 4
    bb1 = bb0 + 62
    draw.rounded_rectangle([RX, bb0, W - 22, bb1], radius=20,
                            fill=(*BOX_BG, 255), outline=(*CYAN, 200), width=2)
    bcy = (bb0 + bb1) // 2
    _circle_icon(draw, RX + 38, bcy, 16, CYAN, "bolt")
    draw.line([(RX + 68, bb0 + 14), (RX + 68, bb1 - 14)],
              fill=(*CYAN_D, 150), width=1)
    draw.text((RX + 80, bcy), "Powered By ",  fill=GREY, font=fnt_brand, anchor="lm")
    pw = draw.textlength("Powered By ", font=fnt_brand)
    draw.text((RX + 80 + pw, bcy), "@SECRECT_BOT_UPDATES", fill=CYAN, font=fnt_brand, anchor="lm")

    return canvas.convert("RGB")


async def _fetch_yt_info(videoid: str) -> dict:
    url     = f"https://www.youtube.com/watch?v={videoid}"
    results = VideosSearch(url, limit=1)
    data    = {}
    for result in (await results.next())["result"]:
        try:
            t = result["title"]
            data["title"] = re.sub(r"\W+", " ", t).strip().title()
        except Exception:
            data["title"] = "Unknown Title"
        data["duration"]  = result.get("duration", "0:00")
        data["thumbnail"] = result["thumbnails"][0]["url"].split("?")[0]
        try:
            data["views"] = result["viewCount"]["short"]
        except Exception:
            data["views"] = "N/A"
    return data


async def _download_cover(url: str, path: str) -> None:
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as r:
            if r.status == 200:
                async with aiofiles.open(path, "wb") as f:
                    await f.write(await r.read())


async def gen_thumb(videoid: str, requester: str = "@MR_ARMAN_08") -> str:
    out_path   = f"cache/{videoid}.png"
    cover_path = f"cache/thumb{videoid}.png"

    if os.path.isfile(out_path):
        return out_path

    try:
        info  = await _fetch_yt_info(videoid)
        await _download_cover(info["thumbnail"], cover_path)

        cover = Image.open(cover_path)
        thumb = _build_thumbnail(
            cover_img=cover,
            title=info["title"],
            views=f"{info['views']} views",
            duration=f"{info['duration']} Mins",
            owner=requester,
        )
        thumb.save(out_path)

    except Exception:
        return YOUTUBE_IMG_URL
    finally:
        try:
            os.remove(cover_path)
        except Exception:
            pass

    return out_path


async def gen_qthumb(videoid: str, requester: str = "@Lord_Vasudev_Krishna") -> str:
    return await gen_thumb(videoid, requester)
