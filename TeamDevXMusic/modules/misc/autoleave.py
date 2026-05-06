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
from datetime import datetime
from pyrogram.enums import ChatType

import config
from TeamDevXMusic import app
from TeamDevXMusic.relay.caller import TeamDevXMusic, autoend
from TeamDevXMusic.toolkit.datastore import (
    get_client,
    is_active_chat,
    is_autoend,
)

autoend = {}


async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT != str(True):
        return
    while not await asyncio.sleep(config.AUTO_LEAVE_ASSISTANT_TIME):
        from TeamDevXMusic.relay.assistant import assistants

        for num in assistants:
            client = await get_client(num)
            try:
                async for i in client.get_dialogs():
                    chat_type = i.chat.type
                    if chat_type in [
                        ChatType.SUPERGROUP,
                        ChatType.GROUP,
                        ChatType.CHANNEL,
                    ]:
                        chat_id = i.chat.id
                        if chat_id not in [
                            config.LOG_GROUP_ID,
                            -1001686672798,
                        ] and not await is_active_chat(chat_id):
                            try:
                                await client.leave_chat(chat_id)
                            except Exception:
                                continue
            except Exception:
                pass


asyncio.create_task(auto_leave())


# async def auto_end():
#     while not await asyncio.sleep(30):
#         if not await is_autoend():
#             continue
#         for chat_id in autoend:
#             timer = autoend.get(chat_id)
#             if not timer:
#                 continue
#             if datetime.now() > timer:
#                 if not await is_active_chat(chat_id):
#                     autoend[chat_id] = {}
#                     continue
#                 autoend[chat_id] = {}
#                 try:
#                     await TeamDevXMusic.stop_stream(chat_id)
#                 except Exception:
#                     continue
#                 try:
#                     await app.send_message(
#                         chat_id,
#                         "» ʙᴏᴛ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴇғᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ʙᴇᴄᴀᴜsᴇ ɴᴏ ᴏɴᴇ ᴡᴀs ʟɪsᴛᴇɴɪɴɢ ᴏɴ ᴠɪᴅᴇᴏᴄʜᴀᴛ.",
#                     )
#                 except Exception:
#                     continue


# asyncio.create_task(auto_end())
