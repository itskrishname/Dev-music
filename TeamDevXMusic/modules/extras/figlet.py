""""
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

from random import choice

import pyfiglet
from pyrogram import filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

_FONTS = [
    "slant", "banner", "big", "block", "bubble", "digital",
    "ivrit", "lean", "mini", "script", "shadow", "small",
    "smscript", "smshadow", "smslant", "standard", "term",
]


def TeamDev_render_figlet(text: str, font: str = "standard") -> str:
    try:
        return pyfiglet.figlet_format(text, font=font)
    except Exception:
        return pyfiglet.figlet_format(text, font="standard")


@app.on_message(filters.command("figlet") & ~BANNED_USERS)
async def mr_d_figlet_command(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "» Please provide some text.\nExample: `/figlet Sᴇᴄʀᴇᴄᴛ 𝐁ᴏᴛ 𝐔ᴘᴅᴀᴛᴇs"
        )

    text = " ".join(message.command[1:])
    font = choice(_FONTS)
    rendered = TeamDev_render_figlet(text, font)

    if not rendered.strip():
        return await message.reply_text("» Could not render that text.")

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 New Font", callback_data=f"figlet_regen:{text}")]
    ])

    await message.reply_text(
        f"```\n{rendered}\n```\nFont: {font} | Powered by @SECRECT_BOT_UPDATES",
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex(r"^figlet_regen:(.+)$"))
async def team_x_og_figlet_regen(_, query: CallbackQuery):
    text = query.data.split(":", 1)[1]
    font = choice(_FONTS)
    rendered = TeamDev_render_figlet(text, font)

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔄 New Font", callback_data=f"figlet_regen:{text}")]
    ])

    try:
        await query.message.edit_text(
            f"```\n{rendered}\n```\nFont: {font} | Powered by @SECRECT_BOT_UPDATES",
            reply_markup=keyboard,
        )
    except Exception:
        pass
    await query.answer()
