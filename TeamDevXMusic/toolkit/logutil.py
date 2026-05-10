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

from pyrogram.enums import ParseMode

from config import LOG_GROUP_ID
from TeamDevXMusic.toolkit.datastore import is_on_off
from TeamDevXMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} 𝖯𝗅𝖺𝗒 𝖫𝗈𝗀</b>

<b>𝖢𝗁𝖺𝗍 𝖨𝖣 :</b> <code>{message.chat.id}</code>
<b>𝖢𝗁𝖺𝗍 𝖭𝖺𝗆𝖾 :</b> {message.chat.title}
<b>𝖢𝗁𝖺𝗍 𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :</b> @{message.chat.username}

<b>𝖴𝗌𝖾𝗋 𝖨𝖣 :</b> <code>{message.from_user.id}</code>
<b>𝖴𝗌𝖾𝗋 𝖭𝖺𝗆𝖾 :</b> {message.from_user.mention}
<b>𝖴𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :</b> @{message.from_user.username}

<b>𝖰𝗎𝖾𝗋𝗒 :</b> {message.text.split(None, 1)[1]}
<b>𝖲𝗍𝗋𝖾𝖺𝗆-𝖳𝗒𝗉𝖾 :</b> {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except Exception:
                pass
        return
