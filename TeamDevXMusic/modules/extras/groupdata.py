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

import time
from asyncio import sleep
from datetime import datetime

from pyrogram import enums, filters
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

@app.on_message(
    ~filters.private & filters.command("groupdata") & ~BANNED_USERS,
    group=2,
)
async def TeamDev_groupdata(_, message: Message):
    chat = message.chat
    start = time.time()

    try:
        full_chat = await _.get_chat(chat.id)
    except Exception as e:
        return await message.reply_text(f"» Failed to fetch group data.\nError: `{e}`")

    admins = bots = 0
    try:
        async for member in _.get_chat_members(chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if member.user.is_bot:
                bots += 1
            else:
                admins += 1
    except Exception:
        pass

    members = getattr(full_chat, "members_count", "N/A")
    description = getattr(full_chat, "description", None) or "No description."
    username = f"@{full_chat.username}" if getattr(full_chat, "username", None) else "Private"
    linked = getattr(full_chat, "linked_chat", None)
    linked_str = f"@{linked.username}" if linked and getattr(linked, "username", None) else "None"
    created = getattr(full_chat, "date", None)
    created_str = created.strftime("%Y-%m-%d") if isinstance(created, datetime) else "Unknown"

    elapsed = round((time.time() - start) * 1000, 2)

    text = (
        f"**» Group Data**\n\n"
        f"» **Name:** {full_chat.title}\n"
        f"» **ID:** `{chat.id}`\n"
        f"» **Username:** {username}\n"
        f"» **Members:** {members:,}\n"
        f"» **Admins:** {admins}\n"
        f"» **Bots:** {bots}\n"
        f"» **Linked Channel:** {linked_str}\n"
        f"» **Created:** {created_str}\n\n"
        f"» **Description:**\n{description}\n\n"
        f"_Fetched in {elapsed}ms | Powered by @Team_X_Og_"
    )

    msg = await message.reply_text(text)
    await sleep(120)
    try:
        await msg.delete()
    except Exception:
        pass
