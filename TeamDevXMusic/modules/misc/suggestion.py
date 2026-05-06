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
import random
from datetime import datetime, timedelta

import config
from config import clean
from strings import get_string
from TeamDevXMusic import app
from TeamDevXMusic.toolkit.datastore import (
    get_lang,
    get_private_served_chats,
    get_served_chats,
    is_suggestion,
)

LEAVE_TIME = config.AUTO_SUGGESTION_TIME


suggestor = {}

strings = [item for item in get_string("en") if item[:3] == "sug" and item != "sug_0"]


async def dont_do_this():
    if config.AUTO_SUGGESTION_MODE != str(True):
        return
    while not await asyncio.sleep(LEAVE_TIME):
        try:
            chats = []
            if config.PRIVATE_BOT_MODE == str(True):
                schats = await get_private_served_chats()
            else:
                schats = await get_served_chats()
            for chat in schats:
                chats.append(int(chat["chat_id"]))
            total = len(chats)
            if total >= 100:
                total //= 10
            send_to = 0
            random.shuffle(chats)
            for x in chats:
                if send_to == total:
                    break
                if x == config.LOG_GROUP_ID:
                    continue
                if not await is_suggestion(x):
                    continue
                try:
                    language = await get_lang(x)
                    _ = get_string(language)
                except Exception:
                    _ = get_string("en")
                string = random.choice(strings)
                if previous := suggestor.get(x):
                    while previous == (string.split("_")[1]):
                        string = random.choice(strings)
                suggestor[x] = string.split("_")[1]
                try:
                    msg = _["sug_0"] + _[string]
                    sent = await app.send_message(x, msg)
                    if x not in clean:
                        clean[x] = []
                    time_now = datetime.now()
                    put = {
                        "msg_id": sent.message_id,
                        "timer_after": time_now
                        + timedelta(minutes=config.CLEANMODE_DELETE_MINS),
                    }
                    clean[x].append(put)
                    send_to += 1
                except Exception:
                    pass
        except Exception:
            pass


asyncio.create_task(dont_do_this())
