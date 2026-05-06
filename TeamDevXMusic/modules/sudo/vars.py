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


import asyncio

from pyrogram import filters

import config
from strings import get_command
from TeamDevXMusic import app
from TeamDevXMusic.helpers import SUDOERS
from TeamDevXMusic.toolkit.datastore.memdb import get_video_limit
from TeamDevXMusic.toolkit.fmt import convert_bytes

VARS_COMMAND = get_command("VARS_COMMAND")


@app.on_message(filters.command(VARS_COMMAND) & SUDOERS)
async def varsFunc(client, message):
    mystic = await message.reply_text("ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ... ɢᴇᴛᴛɪɴɢ ʏᴏᴜʀ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs...")
    v_limit = await get_video_limit()
    bot_name = config.MUSIC_BOT_NAME
    up_r = f"[ʀᴇᴩᴏ]({config.UPSTREAM_REPO})"
    up_b = config.UPSTREAM_BRANCH
    auto_leave = config.AUTO_LEAVE_ASSISTANT_TIME
    yt_sleep = config.YOUTUBE_DOWNLOAD_EDIT_SLEEP
    tg_sleep = config.TELEGRAM_DOWNLOAD_EDIT_SLEEP
    playlist_limit = config.SERVER_PLAYLIST_LIMIT
    fetch_playlist = config.PLAYLIST_FETCH_LIMIT
    song = config.SONG_DOWNLOAD_DURATION
    play_duration = config.DURATION_LIMIT_MIN
    cm = config.CLEANMODE_DELETE_MINS
    auto_sug = config.AUTO_SUGGESTION_TIME
    ass = "ʏᴇs" if config.AUTO_LEAVING_ASSISTANT == str(True) else "ɴᴏ"
    pvt = "ʏᴇs" if config.PRIVATE_BOT_MODE == str(True) else "ɴᴏ"
    a_sug = "ʏᴇs" if config.AUTO_SUGGESTION_MODE == str(True) else "ɴᴏ"
    down = "ʏᴇs" if config.AUTO_DOWNLOADS_CLEAR == str(True) else "ɴᴏ"
    git = f"[ʀᴇᴩᴏ]({config.GITHUB_REPO})" if config.GITHUB_REPO else "ɴᴏ"
    if not config.START_IMG_URL:
        start = "ɴᴏ"
    else:
        start = f"[ɪᴍᴀɢᴇ]({config.START_IMG_URL})"
    if not config.SUPPORT_CHANNEL:
        s_c = "ɴᴏ"
    else:
        s_c = f"[ᴄʜᴀɴɴᴇʟ]({config.SUPPORT_CHANNEL})"
    if not config.SUPPORT_GROUP:
        s_g = "ɴᴏ"
    else:
        s_g = f"[sᴜᴩᴩᴏʀᴛ]({config.SUPPORT_GROUP})"
    if not config.GIT_TOKEN:
        token = "ɴᴏ"
    else:
        token = "ʏᴇs"
    if not config.SPOTIFY_CLIENT_ID and not config.SPOTIFY_CLIENT_SECRET:
        sotify = "ɴᴏ"
    else:
        sotify = "ʏᴇs"
    owners = [str(ids) for ids in config.OWNER_ID]
    owner_id = " ,".join(owners)
    tg_aud = convert_bytes(config.TG_AUDIO_FILESIZE_LIMIT)
    tg_vid = convert_bytes(config.TG_VIDEO_FILESIZE_LIMIT)
    text = f"""**ᴍᴜsɪᴄ ʙᴏᴛ ᴄᴏɴғɪɢ ᴠᴀʀɪᴀʙʟᴇs:**

**<u>ʙᴀsɪᴄ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴍᴜsɪᴄ_ʙᴏᴛ_ɴᴀᴍᴇ** : `{bot_name}`
**ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ** : `{play_duration} ᴍɪɴᴜᴛᴇs`
**sᴏɴɢ_ᴅᴏᴡɴʟᴏᴀᴅ_ᴅᴜʀᴀᴛɪᴏɴ_ʟɪᴍɪᴛ** :` {song} ᴍɪɴᴜᴛᴇs`
**ᴏᴡɴᴇʀ_ɪᴅ** : `{owner_id}`
    
**<u>ʀᴇᴩᴏsɪᴛᴏʀʏ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴜᴩsᴛʀᴇᴀᴍ_ʀᴇᴩᴏ** : `{up_r}`
**ᴜᴩsᴛʀᴇᴀᴍ_ʙʀᴀɴᴄʜ** : `{up_b}`
**ɢɪᴛʜᴜʙ_ʀᴇᴩᴏ** :` {git}`
**ɢɪᴛ_ᴛᴏᴋᴇɴ**:` {token}`


**<u>ʙᴏᴛ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**ᴀᴜᴛᴏ_ʟᴇᴀᴠɪɴɢ_ᴀssɪsᴛᴀɴᴛ** : `{ass}`
**ᴀssɪsᴛᴀɴᴛ_ʟᴇᴀᴠᴇ_ᴛɪᴍᴇ** : `{auto_leave} sᴇᴄᴏɴᴅs`
**ᴀᴜᴛᴏ_sᴜɢɢᴇsᴛɪᴏɴ_ᴍᴏᴅᴇ** :` {a_sug}`
**ᴀᴜᴛᴏ_sᴜɢɢᴇsᴛɪᴏɴ_ᴛɪᴍᴇ** : `{auto_sug} sᴇᴄᴏɴᴅs`
**ᴀᴜᴛᴏ_ᴅᴏᴡɴʟᴏᴀᴅs_ᴄʟᴇᴀʀ** : `{down}`
**ᴩʀɪᴠᴀᴛᴇ_ʙᴏᴛ_ᴍᴏᴅᴇ** : `{pvt}`
**ʏᴏᴜᴛᴜʙᴇ_ᴇᴅɪᴛ_sʟᴇᴇᴩ** : `{yt_sleep} sᴇᴄᴏɴᴅs`
**ᴛᴇʟᴇɢʀᴀᴍ_ᴇᴅɪᴛ_sʟᴇᴇᴩ** :` {tg_sleep} sᴇᴄᴏɴᴅs`
**ᴄʟᴇᴀɴᴍᴏᴅᴇ_ᴍɪɴs** : `{cm} ᴍɪɴᴜᴛᴇs`
**ᴠɪᴅᴇᴏ_sᴛʀᴇᴀᴍ_ʟɪᴍɪᴛ** : `{v_limit} ᴄʜᴀᴛs`
**sᴇʀᴠᴇʀ_ᴩʟᴀʏʟɪsᴛ_ʟɪᴍɪᴛ** :` {playlist_limit}`
**ᴩʟᴀʏʟɪsᴛ_ғᴇᴛᴄʜ_ʟɪᴍɪᴛ** :` {fetch_playlist}`

**<u>sᴩᴏᴛɪғʏ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**sᴩᴏᴛɪғʏ_ᴄʟɪᴇɴᴛ_ɪᴅ** :` {sotify}`
**sᴩᴏᴛɪғʏ_ᴄʟɪᴇɴᴛ_sᴇᴄʀᴇᴛ** : `{sotify}`

**<u>Playsize Vars:</u>**
**ᴛɢ_ᴀᴜᴅɪᴏ_ғʟɪᴇsɪᴢᴇ_ʟɪᴍɪᴛ** :` {tg_aud}`
**ᴛɢ_ᴠɪᴅᴇᴏ_ғɪʟᴇsɪᴢᴇ_ʟɪᴍɪᴛ** :` {tg_vid}`

**<u>ᴇxᴛʀᴀ ᴠᴀʀɪᴀʙʟᴇs:</u>**
**sᴜᴩᴩᴏʀᴛ_ᴄʜᴀɴɴᴇʟ** : `{s_c}`
**sᴜᴩᴩᴏʀᴛ_ɢʀᴏᴜᴩ** : ` {s_g}`
**sᴛᴀʀᴛ_ɪᴍɢ_ᴜʀʟ** : ` {start}`
    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
