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


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from TeamDevXMusic import app


def back_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="TOPMARKUPGET",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def overallback_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GlobalStats",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def get_stats_markup(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_8"],
            callback_data="bot_stats_sudo g",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        ),
    ]
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SA_B_7"],
                    callback_data="TOPMARKUPGET",
                )
            ],
            [
                InlineKeyboardButton(
                    text=_["SA_B_6"],
                    url=f"https://t.me/{app.username}?start=stats",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_5"],
                    callback_data="TopOverall g",
                ),
            ],
            sudo if status else not_sudo,
        ]
    )


def stats_buttons(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["SA_B_5"],
            callback_data="TopOverall s",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_8"],
            callback_data="bot_stats_sudo s",
        ),
        InlineKeyboardButton(
            text=_["SA_B_5"],
            callback_data="TopOverall s",
        ),
    ]
    return InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def back_stats_buttons(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GETSTATS",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def top_ten_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SA_B_2"],
                    callback_data="GetStatsNow Tracks",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_1"],
                    callback_data="GetStatsNow Chats",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["SA_B_3"],
                    callback_data="GetStatsNow Users",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_4"],
                    callback_data="GetStatsNow Here",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GlobalStats",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
