"""
                      [TeamDev](https://t.me/team_x_og)
          
          Project Id -> 39.
          Project Name -> TeamDev X Music
          Project Age -> 15D+ (Updated On 05/05/2026)
          Project Idea By -> @MR_ARMAN_08
          Project Dev -> @MR_ARMAN_08
          Powered By -> @SECRECT_BOT_UPDATES ( On Telegram )
          Updates -> @TeamDevXBots ( On telegram )
    
    Setup Guides -> Read > README.md
    
          This Script Part Off https://t.me/Team_X_Og's Team.
          Copyright ©️ 2026 TeamDev | @SECRECT_BOT_UPDATES
          
    • Some Quick Help
    - Read Full README.md For Understanding The Content.
    - If You Need Any Help Contact Us In @SECRECT_BOT_UPDATES's Group
    
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

import asyncio
from typing import Optional

from pyrogram.types import InlineKeyboardMarkup

import config
from TeamDevXMusic import YouTube, app
from TeamDevXMusic.logcfg import LOGGER
from TeamDevXMusic.helpers import db
from TeamDevXMusic.relay.caller import TeamDevXMusic
from TeamDevXMusic.toolkit.datastore import (
    add_active_chat,
    get_audio_bitrate,
    get_lang,
    get_video_bitrate,
    music_on,
    set_autoplay_last,
)
from TeamDevXMusic.toolkit.engine.trackqueue import put_queue
from TeamDevXMusic.toolkit.panels.play import stream_markup
from TeamDevXMusic.toolkit.thumbgen import gen_thumb
from strings import get_string

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"
_log = LOGGER("TeamDevXMusic.autoplay")

_in_progress: set = set()


async def TeamDev_fetch_related(vidid: str, limit: int = 6) -> list[dict]:
    from yt_dlp import YoutubeDL

    url = f"https://www.youtube.com/watch?v={vidid}"
    opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": "in_playlist",
        "playlist_items": f"1:{limit}",
        "cookiefile": YouTube.cookiefile() if hasattr(YouTube, "cookiefile") else None,
    }
    if opts.get("cookiefile") is None:
        opts.pop("cookiefile", None)

    loop = asyncio.get_event_loop()

    def mr_d_extract():
        with YoutubeDL(opts) as ydl:
            try:
                info = ydl.extract_info(
                    f"https://www.youtube.com/watch?v={vidid}&list=RD{vidid}",
                    download=False,
                )
                entries = info.get("entries", []) if info else []
                results = []
                for e in entries:
                    if not e:
                        continue
                    eid = e.get("id") or e.get("url", "").split("v=")[-1]
                    if not eid or eid == vidid:
                        continue
                    title = e.get("title", "Unknown")
                    dur = e.get("duration")
                    if dur and dur > config.DURATION_LIMIT:
                        continue
                    dur_min = (
                        f"{int(dur)//60:02d}:{int(dur)%60:02d}" if dur else "Unknown"
                    )
                    thumb = (
                        f"https://img.youtube.com/vi/{eid}/hqdefault.jpg"
                    )
                    results.append(
                        {
                            "title": title,
                            "vidid": eid,
                            "duration_min": dur_min,
                            "thumb": thumb,
                            "link": f"https://youtu.be/{eid}",
                        }
                    )
                return results
            except Exception as ex:
                _log.warning(f"yt-dlp related extraction failed: {ex}")
                return []

    return await loop.run_in_executor(None, mr_d_extract)


async def team_x_og_fallback_search(title: str) -> Optional[dict]:
    try:
        track, _ = await YouTube.track(title)
        return track
    except Exception as ex:
        _log.warning(f"Fallback search failed for '{title}': {ex}")
        return None


async def TeamDev_trigger_autoplay(client, chat_id: int, last_vidid: str):
    if chat_id in _in_progress:
        return
    _in_progress.add(chat_id)

    try:
        _log.info(f"[AutoPlay] Fetching related for {last_vidid} in chat {chat_id}")

        related = await TeamDev_fetch_related(last_vidid, limit=8)

        chosen: Optional[dict] = None
        for candidate in related:
            chosen = candidate
            break

        if not chosen:
            _log.info(f"[AutoPlay] No related found, using search fallback")
            try:
                _, _ = await YouTube.details(last_vidid, videoid=True)
            except Exception:
                pass
            chosen = await team_x_og_fallback_search(last_vidid)

        if not chosen:
            _log.warning(f"[AutoPlay] Could not find a related track for {last_vidid}")
            return await client.leave_call(chat_id)

        vidid = chosen["vidid"]
        title = chosen.get("title", "AutoPlay Track").title()
        duration_min = chosen.get("duration_min", "Unknown")
        thumbnail = chosen.get("thumb", config.YOUTUBE_IMG_URL)

        original_chat_id = chat_id

        language = await get_lang(chat_id)
        _ = get_string(language)

        notify_msg = await app.send_message(
            original_chat_id,
            f"**AutoPlay** | Fetching next track…\n🎵 **{title[:50]}**\n\nPowered by @SECRECT_BOT_UPDATES",
        )

        try:
            file_path, direct = await YouTube.download(
                vidid, notify_msg, videoid=True, video=None
            )
        except Exception as dl_err:
            _log.warning(f"[AutoPlay] Download failed: {dl_err}")
            await notify_msg.edit_text("» AutoPlay: Failed to download next track.")
            return await client.leave_call(chat_id)

        audio_quality = await get_audio_bitrate(chat_id)
        video_quality = await get_video_bitrate(chat_id)

        try:
            await TeamDevXMusic.join_call(
                chat_id,
                original_chat_id,
                file_path,
                video=None,
                image=thumbnail,
            )
        except Exception as vc_err:
            _log.warning(f"[AutoPlay] join_call failed: {vc_err}")
            await notify_msg.edit_text("» AutoPlay: Could not join voice chat.")
            return

        db[chat_id] = []
        await put_queue(
            chat_id,
            original_chat_id,
            file_path if direct else f"vid_{vidid}",
            title,
            duration_min,
            "AutoPlay",
            vidid,
            0,
            "audio",
        )
        await music_on(chat_id)
        await add_active_chat(chat_id)

        set_autoplay_last(chat_id, vidid)

        img = await gen_thumb(vidid)
        button = stream_markup(_, vidid, chat_id)
        await notify_msg.delete()
        run = await app.send_photo(
            original_chat_id,
            photo=img,
            caption=(
                f"**AutoPlay**\n\n"
                f"🎵 **[{title[:40]}](https://t.me/{app.username}?start=info_{vidid})**\n"
                f"⏱ **Duration:** {duration_min}\n"
                f"🤖 **Queued by:** AutoPlay\n\n"
                f"Powered by @SECRECT_BOT_UPDATES"
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "stream"

    except Exception as e:
        _log.error(f"[AutoPlay] Unexpected error for chat {chat_id}: {e}")
        try:
            await client.leave_call(chat_id)
        except Exception:
            pass
    finally:
        _in_progress.discard(chat_id)
