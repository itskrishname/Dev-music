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


import sys

from pyrogram import Client

import config

from ..logcfg import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="TeamDevOne",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            name="TeamDevTwo",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            name="TeamDevThree",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            name="TeamDevFour",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            name="TeamDevFive",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant Clients...")
        if config.STRING1:
            await self.one.start()
            try:
                pass
            except Exception:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = get_me.first_name + " " + get_me.last_name
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")
        if config.STRING2:
            await self.two.start()
            try:
                pass
            except Exception:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = get_me.first_name + " " + get_me.last_name
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")
        if config.STRING3:
            await self.three.start()
            try:
                pass
            except Exception:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = get_me.first_name + " " + get_me.last_name
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")
        if config.STRING4:
            await self.four.start()
            try:
                pass
            except Exception:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = get_me.first_name + " " + get_me.last_name
            else:
                self.four.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Four Started as {self.four.name}")
        if config.STRING5:
            await self.five.start()
            try:
                pass
            except Exception:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID,
                    "ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ, ɴᴏᴡ ɪᴛ's ᴛɪᴍᴇ ᴛᴏ ᴇɴᴊᴏʏ ᴍᴜsɪᴄ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ᴠɪᴅᴇᴏᴄʜᴀᴛs.",
                )
            except Exception:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = get_me.first_name + " " + get_me.last_name
            else:
                self.five.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Five Started as {self.five.name}")
