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
import glob
import importlib
import os
import sys
from typing import Any

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from TeamDevXMusic import LOGGER, app, userbot
from TeamDevXMusic.relay.caller import TeamDevXMusic
from TeamDevXMusic.helpers import sudo
from TeamDevXMusic.modules import ALL_MODULES
from TeamDevXMusic.toolkit.datastore import get_banned_users, get_gbanned
from TeamDevXMusic.relay.cookiejar import save_cookies


async def init() -> None:
    if all(not getattr(config, f"STRING{i}") for i in range(1, 6)):
        LOGGER("TeamDevXMusic").error("Add Pyrogram string session and then try...")
        exit()
    await sudo()
    try:
        for user_id in await get_gbanned():
            BANNED_USERS.add(user_id)
        for user_id in await get_banned_users():
            BANNED_USERS.add(user_id)
    except Exception:
        pass
    await app.start()
    await save_cookies()
    for module in ALL_MODULES:
        importlib.import_module(f"TeamDevXMusic.modules{module}")
    LOGGER("TeamDevXMusic.modules").info("Necessary Modules Imported Successfully.")
    await userbot.start()
    await TeamDevXMusic.start()
    try:
        await TeamDevXMusic.stream_call("https://telegra.ph/file/b60b80ccb06f7a48f68b5.mp4")
    except NoActiveGroupCall:
        LOGGER("TeamDevXMusic").error(
            "[ERROR] - \n\nTurn on group voice chat and don't put it off otherwise I'll stop working thanks."
        )
        exit()
    except Exception:
        pass
    await TeamDevXMusic.decorators()
    LOGGER("TeamDevXMusic").info("TeamDevXMusic Bot Started Successfully")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("TeamDevXMusic").info("Stopping TeamDevXMusic Bot...")


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(init())
        LOGGER("TeamDevXMusic").info("Stopping Music Bot")
    except Exception as e:
        if "database is locked" in str(e) or "is_initialized" in str(e):
            LOGGER("TeamDevXMusic").warning(
                f"Session error detected: {e}\nDeleting .session files and restarting..."
            )
            for sf in glob.glob("*.session") + glob.glob("*.session-journal"):
                try:
                    os.remove(sf)
                    LOGGER("TeamDevXMusic").info(f"Deleted: {sf}")
                except Exception:
                    pass
            os.execv(sys.executable, [sys.executable, "-m", "TeamDevXMusic"])
        else:
            raise
