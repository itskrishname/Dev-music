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


from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

import config
from config import BANNED_USERS
from strings import get_command
from TeamDevXMusic import YouTube, app
from TeamDevXMusic.relay.caller import TeamDevXMusic
from TeamDevXMusic.helpers import db
from TeamDevXMusic.toolkit.datastore import get_loop
from TeamDevXMusic.toolkit.guards import AdminRightsCheck
from TeamDevXMusic.toolkit.panels.play import stream_markup, telegram_markup
from TeamDevXMusic.toolkit.engine.cleaner import auto_clean
from TeamDevXMusic.toolkit.thumbgen import gen_thumb

SKIP_COMMAND = get_command("SKIP_COMMAND")


@app.on_message(filters.command(SKIP_COMMAND) & filters.group & ~BANNED_USERS)
@AdminRightsCheck
async def skip(cli, message: Message, _, chat_id):
    if not len(message.command) < 2:
        loop = await get_loop(chat_id)
        if loop != 0:
            return await message.reply_text(_["admin_12"])
        state = message.text.split(None, 1)[1].strip()
        if state.isnumeric():
            state = int(state)
            check = db.get(chat_id)
            if check:
                count = len(check)
                if count > 2:
                    count = int(count - 1)
                    if 1 <= state <= count:
                        for x in range(state):
                            popped = None
                            try:
                                popped = check.pop(0)
                            except Exception:
                                return await message.reply_text(_["admin_16"])
                            if popped and config.AUTO_DOWNLOADS_CLEAR == str(True):
                                await auto_clean(popped)
                            if not check:
                                try:
                                    await message.reply_text(
                                        _["admin_10"].format(
                                            message.from_user.first_name
                                        ),
                                        disable_web_page_preview=True,
                                    )
                                    await TeamDevXMusic.stop_stream(chat_id)
                                except Exception:
                                    return
                                break
                    else:
                        return await message.reply_text(_["admin_15"].format(count))
                else:
                    return await message.reply_text(_["admin_14"])
            else:
                return await message.reply_text(_["queue_2"])
        else:
            return await message.reply_text(_["admin_13"])
    else:
        check = db.get(chat_id)
        popped = None
        try:
            if popped := check.pop(0):
                if config.AUTO_DOWNLOADS_CLEAR == str(True):
                    await auto_clean(popped)
            if not check:
                await message.reply_text(
                    _["admin_10"].format(message.from_user.first_name),
                    disable_web_page_preview=True,
                )
                try:
                    return await TeamDevXMusic.stop_stream(chat_id)
                except Exception:
                    return
        except Exception:
            try:
                await message.reply_text(
                    _["admin_10"].format(message.from_user.first_name),
                    disable_web_page_preview=True,
                )
                return await TeamDevXMusic.stop_stream(chat_id)
            except Exception:
                return
    queued = check[0]["file"]
    title = (check[0]["title"]).title()
    user = check[0]["by"]
    user_id = message.from_user.id
    streamtype = check[0]["streamtype"]
    videoid = check[0]["vidid"]
    duration_min = check[0]["dur"]
    status = True if str(streamtype) == "video" else None
    if "live_" in queued:
        n, link = await YouTube.video(videoid, True)
        if n == 0:
            return await message.reply_text(_["admin_11"].format(title))
        try:
            await TeamDevXMusic.skip_stream(chat_id, link, video=status)
        except Exception:
            return await message.reply_text(_["call_9"])
        button = telegram_markup(_, chat_id)
        img = await gen_thumb(videoid)
        run = await message.reply_photo(
            photo=img,
            caption=_["stream_1"].format(
                user,
                f"https://t.me/{app.username}?start=info_{videoid}",
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
    elif "vid_" in queued:
        mystic = await message.reply_text(_["call_10"], disable_web_page_preview=True)
        try:
            file_path, direct = await YouTube.download(
                videoid,
                mystic,
                videoid=True,
                video=status,
            )
        except Exception:
            return await mystic.edit_text(_["call_9"])
        try:
            await TeamDevXMusic.skip_stream(chat_id, file_path, video=status)
        except Exception:
            return await mystic.edit_text(_["call_9"])
        button = stream_markup(_, videoid, chat_id)
        img = await gen_thumb(videoid)
        run = await message.reply_photo(
            photo=img,
            caption=_["stream_1"].format(
                title[:27],
                f"https://t.me/{app.username}?start=info_{videoid}",
                duration_min,
                user,
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "stream"
        await mystic.delete()
    elif "index_" in queued:
        try:
            await TeamDevXMusic.skip_stream(chat_id, videoid, video=status)
        except Exception:
            return await message.reply_text(_["call_9"])
        button = telegram_markup(_, chat_id)
        run = await message.reply_photo(
            photo=config.STREAM_IMG_URL,
            caption=_["stream_2"].format(user),
            reply_markup=InlineKeyboardMarkup(button),
        )
        db[chat_id][0]["mystic"] = run
        db[chat_id][0]["markup"] = "tg"
    else:
        try:
            await TeamDevXMusic.skip_stream(chat_id, queued, video=status)
        except Exception:
            return await message.reply_text(_["call_9"])
        if videoid == "telegram":
            button = telegram_markup(_, chat_id)
            run = await message.reply_photo(
                photo=(
                    config.TELEGRAM_AUDIO_URL
                    if str(streamtype) == "audio"
                    else config.TELEGRAM_VIDEO_URL
                ),
                caption=_["stream_3"].format(title, check[0]["dur"], user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
        elif videoid == "soundcloud":
            button = telegram_markup(_, chat_id)
            run = await message.reply_photo(
                photo=(
                    config.SOUNCLOUD_IMG_URL
                    if str(streamtype) == "audio"
                    else config.TELEGRAM_VIDEO_URL
                ),
                caption=_["stream_3"].format(title, check[0]["dur"], user),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "tg"
        else:
            button = stream_markup(_, videoid, chat_id)
            img = await gen_thumb(videoid)
            run = await message.reply_photo(
                photo=img,
                caption=_["stream_1"].format(
                    title[:27],
                    f"https://t.me/{app.username}?start=info_{videoid}",
                    duration_min,
                    user,
                ),
                reply_markup=InlineKeyboardMarkup(button),
            )
            db[chat_id][0]["mystic"] = run
            db[chat_id][0]["markup"] = "stream"
