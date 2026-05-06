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

import httpx
from pyrogram import filters, enums
from pyrogram.types import Message

from config import BANNED_USERS
from TeamDevXMusic import app


TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

_WEATHER_APIKEY = "8de2d8b3a93542c9a2d8b3a935a2c909"
_COORDS_URL = "https://api.weather.com/v3/location/search"
_WEATHER_URL = "https://api.weather.com/v3/aggcommon/v3-wx-observations-current"
_HEADERS = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 12; M2012K11AG Build/SQ1D.211205.017)"
}


@app.on_message(filters.command("weather") & ~BANNED_USERS)
async def TeamDev_weather_command(_, message: Message):
    if len(message.command) == 1:
        return await message.reply_text(
            "<b>ᴜsᴀɢᴇ:</b> <code>/weather city</code>\n"
            "Example: <code>/weather Delhi</code>",
            parse_mode=enums.ParseMode.HTML,
        )

    query = message.text.split(maxsplit=1)[1]

    try:
        async with httpx.AsyncClient(timeout=40.0) as http:
            coord_resp = await http.get(
                _COORDS_URL,
                headers=_HEADERS,
                params={
                    "apiKey": _WEATHER_APIKEY,
                    "format": "json",
                    "language": "en",
                    "query": query,
                },
            )
            coord_data = coord_resp.json()

            if not coord_data.get("location"):
                return await message.reply_text(
                    "» <b>Location not found.</b> Please try a different city.",
                    parse_mode=enums.ParseMode.HTML,
                )

            lat = coord_data["location"]["latitude"][0]
            lon = coord_data["location"]["longitude"][0]
            loc_name = coord_data["location"]["address"][0]

            wx_resp = await http.get(
                _WEATHER_URL,
                headers=_HEADERS,
                params={
                    "apiKey": _WEATHER_APIKEY,
                    "format": "json",
                    "language": "en",
                    "geocode": f"{lat},{lon}",
                    "units": "m",
                },
            )
            wx_data = wx_resp.json()

        obs = wx_data.get("v3-wx-observations-current", {})
        if not obs:
            return await message.reply_text(
                "» <b>Weather data not available</b> at the moment.",
                parse_mode=enums.ParseMode.HTML,
            )

        text = (
            f"<b>{loc_name}</b>\n\n"
            f"» <b>ᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴇ:</b> <code>{obs.get('temperature', 'N/A')} °C</code>\n"
            f"» <b>ғᴇᴇʟs ʟɪᴋᴇ:</b> <code>{obs.get('temperatureFeelsLike', 'N/A')} °C</code>\n"
            f"» <b>ʜᴜᴍɪᴅɪᴛʏ:</b> <code>{obs.get('relativeHumidity', 'N/A')}%</code>\n"
            f"» <b>ᴡɪɴᴅ:</b> <code>{obs.get('windSpeed', 'N/A')} km/h</code>\n"
            f"» <b>ᴄᴏɴᴅɪᴛɪᴏɴ:</b> <i>{obs.get('wxPhraseLong', 'N/A')}</i>\n\n"
            f"<i>Powered by @Team_X_Og</i>"
        )
        await message.reply_text(text, parse_mode=enums.ParseMode.HTML)

    except Exception as e:
        print(f"[Weather Error] {e}")
        await message.reply_text(
            "» <b>An error occurred</b> while fetching the weather. Please try again later.",
            parse_mode=enums.ParseMode.HTML,
        )
