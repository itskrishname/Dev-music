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
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from TeamDevXMusic import app
from TeamDevXMusic.helpers import SUDOERS
from TeamDevXMusic.toolkit.datastore import add_gban_user, remove_gban_user
from TeamDevXMusic.toolkit.guards.language import language

BLOCK_COMMAND = get_command("BLOCK_COMMAND")
UNBLOCK_COMMAND = get_command("UNBLOCK_COMMAND")
BLOCKED_COMMAND = get_command("BLOCKED_COMMAND")


@app.on_message(filters.command(BLOCK_COMMAND) & SUDOERS)
@language
async def useradd(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id in BANNED_USERS:
            return await message.reply_text(_["block_1"].format(user.mention))
        await add_gban_user(user.id)
        BANNED_USERS.add(user.id)
        await message.reply_text(_["block_2"].format(user.mention))
        return
    if message.reply_to_message.from_user.id in BANNED_USERS:
        return await message.reply_text(
            _["block_1"].format(message.reply_to_message.from_user.mention)
        )
    await add_gban_user(message.reply_to_message.from_user.id)
    BANNED_USERS.add(message.reply_to_message.from_user.id)
    await message.reply_text(
        _["block_2"].format(message.reply_to_message.from_user.mention)
    )


@app.on_message(filters.command(UNBLOCK_COMMAND) & SUDOERS)
@language
async def userdel(client, message: Message, _):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text(_["general_1"])
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id not in BANNED_USERS:
            return await message.reply_text(_["block_3"])
        await remove_gban_user(user.id)
        BANNED_USERS.remove(user.id)
        await message.reply_text(_["block_4"])
        return
    user_id = message.reply_to_message.from_user.id
    if user_id not in BANNED_USERS:
        return await message.reply_text(_["block_3"])
    await remove_gban_user(user_id)
    BANNED_USERS.remove(user_id)
    await message.reply_text(_["block_4"])


@app.on_message(filters.command(BLOCKED_COMMAND) & SUDOERS)
@language
async def sudoers_list(client, message: Message, _):
    if not BANNED_USERS:
        return await message.reply_text(_["block_5"])
    mystic = await message.reply_text(_["block_6"])
    msg = _["block_7"]
    count = 0
    for users in BANNED_USERS:
        try:
            user = await app.get_users(users)
            user = user.mention or user.first_name
            count += 1
        except Exception:
            continue
        msg += f"{count}➤ {user}\n"
    if count == 0:
        return await mystic.edit_text(_["block_5"])
    else:
        return await mystic.edit_text(msg)
