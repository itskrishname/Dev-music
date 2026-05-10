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
import html
import ipaddress

import httpx
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS
from TeamDevXMusic import app

TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

_IPINFO_TOKEN = "6274faab58da61"
_IPQS_KEY = "952ztTq41AxoXam43pStVjVNcEjo1ntQ"


def _flag(cc: str | None) -> str:
    if not cc or len(cc) != 2:
        return "»"
    return "".join(chr(0x1F1E6 + ord(c) - 65) for c in cc.upper())


def _score_badge(score: int | None) -> tuple:
    if score is None:
        return "» Unknown", "» 0/100"
    blocks = max(0, min(10, round(score / 10)))
    bar = "»" * blocks + "»" * (10 - blocks)
    label = "» Low Risk" if score <= 20 else ("» Medium Risk" if score <= 60 else "» High Risk")
    return label, f"{bar} {score}/100"


def _esc(v) -> str:
    return html.escape(str(v) if v else "N/A")


def _split_asn(org: str | None) -> tuple:
    if not org:
        return "N/A", "N/A"
    parts = org.split(maxsplit=1)
    if parts and parts[0].startswith("AS"):
        return parts[0], parts[1] if len(parts) > 1 else "N/A"
    return "N/A", org


def TeamDev_build_ip_card(ip: str, info: dict, score: int | None):
    country = info.get("country")
    flag = _flag(country)
    city, region = info.get("city"), info.get("region")
    loc = info.get("loc", "")
    org = info.get("org")
    timezone = info.get("timezone")
    postal = info.get("postal")
    asn, isp = _split_asn(org)
    badge, bar = _score_badge(score)

    s_ip = _esc(ip)
    maps_url = f"https://maps.google.com/?q={loc.replace(' ', '')}" if loc else f"https://duckduckgo.com/?q={s_ip}"

    text = (
        "<b>» IP Intelligence</b>\n"
        f"{flag} <b>{s_ip}</b>\n\n"
        f"» <b>Risk</b> : {badge}\n"
        f"» <code>{bar}</code>\n\n"
        f"» <b>City</b> : <code>{_esc(city)}</code>\n"
        f"» <b>Region</b> : <code>{_esc(region)}</code>\n"
        f"» <b>Country</b> : <code>{_esc(country)}</code>\n"
        f"» <b>Postal</b> : <code>{_esc(postal)}</code>\n"
        f"» <b>Timezone</b> : <code>{_esc(timezone)}</code>\n"
        f"» <b>ISP</b> : <code>{_esc(isp)}</code>\n"
        f"» <b>ASN</b> : <code>{_esc(asn)}</code>\n"
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("» Maps", url=maps_url),
            InlineKeyboardButton("ℹ ipinfo", url=f"https://ipinfo.io/{s_ip}"),
        ],
        [
            InlineKeyboardButton("» IPQualityScore", url=f"https://www.ipqualityscore.com/free-ip-lookup-proxy-vpn-test/lookup/{s_ip}"),
            InlineKeyboardButton("» AbuseIPDB", url=f"https://www.abuseipdb.com/check/{s_ip}"),
        ],
    ])
    return text, keyboard


async def mr_d_fetch_ipinfo(client: httpx.AsyncClient, ip: str) -> dict | None:
    try:
        r = await client.get(f"https://ipinfo.io/{ip}?token={_IPINFO_TOKEN}", timeout=10)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


async def team_x_og_fetch_ipqs(client: httpx.AsyncClient, ip: str) -> int | None:
    try:
        r = await client.get(
            f"https://ipqualityscore.com/api/json/ip/{_IPQS_KEY}/{ip}", timeout=12
        )
        if r.status_code == 200:
            fs = r.json().get("fraud_score")
            return int(fs) if str(fs).isdigit() else None
    except Exception:
        pass
    return None


@app.on_message(filters.command("ip") & ~BANNED_USERS)
async def TeamDev_ip_lookup(_, message: Message):
    if len(message.command) != 2:
        return await message.reply_text(
            "» Please provide an IP address.\nExample: <code>/ip 8.8.8.8</code>",
            disable_web_page_preview=True,
        )

    ip_raw = message.command[1].strip()
    try:
        ip_obj = ipaddress.ip_address(ip_raw)
        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_reserved or ip_obj.is_multicast:
            return await message.reply_text(
                "» That's a <b>non-routable / private</b> address. Please provide a public IP."
            )
    except ValueError:
        return await message.reply_text(
            "» Invalid IP format. Example: <code>/ip 1.1.1.1</code>"
        )

    wait_msg = await message.reply_text("» Analyzing IP… <i>fetching intelligence</i>")

    async with httpx.AsyncClient(headers={"User-Agent": "TeamDevXMusic/IpIntel/1.0"}) as client:
        ipinfo, score = await asyncio.gather(
            mr_d_fetch_ipinfo(client, ip_raw),
            team_x_og_fetch_ipqs(client, ip_raw),
        )

    if not ipinfo and score is None:
        return await wait_msg.edit_text(
            "» Unable to fetch details for this IP. Please try again later."
        )

    text, keyboard = TeamDev_build_ip_card(ip_raw, ipinfo or {}, score)
    await wait_msg.edit_text(
        text, reply_markup=keyboard, disable_web_page_preview=True
    )
