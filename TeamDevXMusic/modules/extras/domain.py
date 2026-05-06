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

import socket
from datetime import datetime, timezone

import requests
import whois
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app


TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

def TeamDev_get_whois(domain_name: str):
    try:
        return whois.whois(domain_name)
    except Exception as e:
        print(f"[WHOIS Error] {e}")
        return None


def mr_d_get_domain_age(creation_date) -> int | None:
    if isinstance(creation_date, list):
        creation_date = creation_date[0]
    if not creation_date:
        return None
    try:
        if hasattr(creation_date, "tzinfo") and creation_date.tzinfo is not None:
            creation_date = creation_date.replace(tzinfo=None)
        return (datetime.now() - creation_date).days // 365
    except Exception:
        return None


def team_x_og_get_ip_location(ip: str) -> dict | None:
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=8)
        if resp.ok:
            data = resp.json()
            return data if data.get("status") == "success" else None
    except Exception as e:
        print(f"[IP Geo Error] {e}")
    return None


def TeamDev_format_domain_info(info) -> str:
    def clean(item):
        if isinstance(item, list):
            return item[0] if item else None
        return item

    domain = clean(info.domain_name)
    registrar = clean(info.registrar)
    creation = clean(info.creation_date)
    expiry = clean(info.expiration_date)
    nameservers = ", ".join(info.name_servers) if info.name_servers else "N/A"
    age = mr_d_get_domain_age(creation)

    try:
        ip = socket.gethostbyname(domain)
    except Exception:
        ip = "Unavailable"

    loc_data = team_x_og_get_ip_location(ip)
    location = f"{loc_data['country']}, {loc_data['city']}" if loc_data else "Unavailable"

    return (
        f"**ᴅᴏᴍᴀɪɴ ɴᴀᴍᴇ**: {domain}\n"
        f"**ʀᴇɢɪsᴛʀᴀʀ**: {registrar}\n"
        f"**ᴄʀᴇᴀᴛɪᴏɴ ᴅᴀᴛᴇ**: {creation.strftime('%Y-%m-%d') if creation else 'N/A'}\n"
        f"**ᴇxᴘɪʀᴀᴛɪᴏɴ ᴅᴀᴛᴇ**: {expiry.strftime('%Y-%m-%d') if expiry else 'N/A'}\n"
        f"**ᴅᴏᴍᴀɪɴ ᴀɢᴇ**: {age} years\n"
        f"**ɪᴘ ᴀᴅᴅʀᴇss**: `{ip}`\n"
        f"**ʟᴏᴄᴀᴛɪᴏɴ**: {location}\n"
        f"**ɴᴀᴍᴇsᴇʀᴠᴇʀs**: {nameservers}\n\n"
        f"_Powered by @Team_X_Og_"
    )


@app.on_message(filters.command("domain") & ~BANNED_USERS)
async def mr_d_domain_lookup(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text(
            "» Please provide a domain name.\nExample: `/domain google.com`"
        )

    domain_name = message.text.split(maxsplit=1)[1].strip()
    wait = await message.reply_text("» Fetching WHOIS data…")

    try:
        data = TeamDev_get_whois(domain_name)
        if not data:
            return await wait.edit_text(
                "» Failed to retrieve WHOIS data.\n"
                "The domain may not exist or the WHOIS server is unreachable."
            )
        await wait.edit_text(TeamDev_format_domain_info(data))
    except Exception as e:
        print(f"[Domain Lookup Error] {e}")
        await wait.edit_text(
            "» An error occurred while fetching domain info.\n"
            "Please try again later."
        )
