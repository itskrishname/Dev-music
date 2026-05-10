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

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"


@app.on_message(filters.command("dice") & ~BANNED_USERS)
async def TeamDev_roll_dice(_, message: Message):
    try:
        x = await _.send_dice(message.chat.id, "\U0001f3b2")  # 🎲
        await message.reply_text(
            f"Hey {message.from_user.mention}, your score is: **{x.dice.value}**",
            quote=True,
        )
    except Exception as e:
        await message.reply_text(f"» Error: {e}")


@app.on_message(filters.command("dart") & ~BANNED_USERS)
async def mr_d_throw_dart(_, message: Message):
    try:
        x = await _.send_dice(message.chat.id, "\U0001f3af")  # 🎯
        await message.reply_text(
            f"Hey {message.from_user.mention}, your score is: **{x.dice.value}**",
            quote=True,
        )
    except Exception as e:
        await message.reply_text(f"» Error: {e}")


@app.on_message(filters.command("basket") & ~BANNED_USERS)
async def team_x_og_shoot_basket(_, message: Message):
    try:
        x = await _.send_dice(message.chat.id, "\U0001f3c0")  # 🏀
        await message.reply_text(
            f"Hey {message.from_user.mention}, your score is: **{x.dice.value}**",
            quote=True,
        )
    except Exception as e:
        await message.reply_text(f"» Error: {e}")


@app.on_message(filters.command("jackpot") & ~BANNED_USERS)
async def TeamDev_spin_jackpot(_, message: Message):
    try:
        x = await _.send_dice(message.chat.id, "\U0001f3b0")  # 🎰
        await message.reply_text(
            f"Hey {message.from_user.mention}, your score is: **{x.dice.value}**",
            quote=True,
        )
    except Exception as e:
        await message.reply_text(f"» Error: {e}")


@app.on_message(filters.command("ball") & ~BANNED_USERS)
async def mr_d_roll_ball(_, message: Message):
    try:
        x = await _.send_dice(message.chat.id, "\U0001f3b3")  # 🎳
        await message.reply_text(
            f"Hey {message.from_user.mention}, your score is: **{x.dice.value}**",
            quote=True,
        )
    except Exception as e:
        await message.reply_text(f"» Error: {e}")


@app.on_message(filters.command("football") & ~BANNED_USERS)
async def team_x_og_kick_football(_, message: Message):
    try:
        x = await _.send_dice(message.chat.id, "\u26bd")  # ⚽
        await message.reply_text(
            f"Hey {message.from_user.mention}, your score is: **{x.dice.value}**",
            quote=True,
        )
    except Exception as e:
        await message.reply_text(f"» Error: {e}")
