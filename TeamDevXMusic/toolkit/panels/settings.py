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

import config
from typing import Union

from pyrogram.types import InlineKeyboardButton


def setting_markup(_):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_1"], callback_data="AQ"),
            InlineKeyboardButton(text=_["ST_B_2"], callback_data="VQ"),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_3"], callback_data="AU"),
            InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG"),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_5"], callback_data="PM"),
            InlineKeyboardButton(text=_["ST_B_7"], callback_data="CM"),
        ],
        [
            InlineKeyboardButton(
                text="𝖲𝗎𝗉𝗉𝗈𝗋𝗍",
                url=config.SUPPORT_GROUP,
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def audio_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_8"].format("✅") if low == True else _["ST_B_8"].format("")
                ),
                callback_data="LQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_9"].format("✅")
                    if medium == True
                    else _["ST_B_9"].format("")
                ),
                callback_data="MQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_10"].format("✅")
                    if high == True
                    else _["ST_B_10"].format("")
                ),
                callback_data="HQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def video_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_11"].format("✅")
                    if low == True
                    else _["ST_B_11"].format("")
                ),
                callback_data="LQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_12"].format("✅")
                    if medium == True
                    else _["ST_B_12"].format("")
                ),
                callback_data="MQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=(
                    _["ST_B_13"].format("✅")
                    if high == True
                    else _["ST_B_13"].format("")
                ),
                callback_data="HQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def cleanmode_settings_markup(
    _,
    status: Union[bool, str] = None,
    dels: Union[bool, str] = None,
    sug: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_7"], callback_data="CMANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_14"] if status == True else _["ST_B_15"],
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_26"], callback_data="COMMANDANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_14"] if dels == True else _["ST_B_15"],
                callback_data="COMMANDELMODE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_27"], callback_data="SUGGANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_14"] if sug == True else _["ST_B_15"],
                callback_data="SUGGESTIONCHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def auth_users_markup(_, status: Union[bool, str] = None):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_3"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_16"] if status == True else _["ST_B_17"],
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_18"], callback_data="AUTHLIST"),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    return [
        [
            InlineKeyboardButton(text=_["ST_B_19"], callback_data="SEARCHANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_20"] if Direct == True else _["ST_B_21"],
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_22"], callback_data="AUTHANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_16"] if Group == True else _["ST_B_17"],
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(text=_["ST_B_25"], callback_data="PLAYTYPEANSWER"),
            InlineKeyboardButton(
                text=_["ST_B_16"] if Playtype == True else _["ST_B_17"],
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
