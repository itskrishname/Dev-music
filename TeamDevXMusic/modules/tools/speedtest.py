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
import speedtest
from pyrogram import filters
from strings import get_command
from TeamDevXMusic import app
from TeamDevXMusic.helpers import SUDOERS

SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


async def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        await m.edit("<b>⇆ 𝖱𝗎𝗇𝗇𝗂𝗇𝗀 𝖣𝗈𝗐𝗅𝗈𝖺𝖽 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 ...</b>")
        test.download()
        await m.edit("<b>⇆ 𝖱𝗎𝗇𝗇𝗂𝗇𝗀 𝖴𝗉𝗅𝗈𝖺𝖽 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 ...</b>")
        test.upload()
        test.results.share()
        result = test.results.dict()
        await m.edit("<b>↻ 𝖲𝗁𝖺𝗋𝗂𝗇𝗀 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 𝖱𝖾𝗌𝗎𝗅𝗍𝗌 ...</b>")
    except Exception as e:
        return await m.edit(str(e))
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("» 𝖱𝗎𝗇𝗇𝗂𝗇𝗀 𝖠 𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 ...")
    result = await testspeed(m)
    output = f"""✯ <b>𝖲𝗉𝖾𝖾𝖽𝖳𝖾𝗌𝗍 𝖱𝖾𝗌𝗎𝗅𝗍𝗌</b> ✯

<u><b>𝖢𝗅𝗂𝖾𝗇𝗍 :</b></u>
<b>» 𝖨𝖲𝖯 :</b> {result['client']['isp']}
<b>» 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 :</b> {result['client']['country']}

<u><b>𝖲𝖾𝗋𝗏𝖾𝗋 :</b></u>
<b>» 𝖭𝖺𝗆𝖾 :</b> {result['server']['name']}
<b>» 𝖢𝗈𝗎𝗇𝗍𝗋𝗒 :</b> {result['server']['country']}, {result['server']['cc']}
<b>» 𝖲𝗉𝗈𝗇𝗌𝗈𝗋 :</b> {result['server']['sponsor']}
<b>» 𝖫𝖺𝗍𝖾𝗇𝖼𝗒 :</b> {result['server']['latency']} 
<b>» 𝖯𝗂𝗇𝗀 :</b> {result['ping']}
"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
