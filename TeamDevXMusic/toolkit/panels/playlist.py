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


def botplaylist_markup(_):
    return [
        [
            InlineKeyboardButton(
                text=_["PL_B_1"],
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(text=_["PL_B_8"], callback_data="get_top_playlists"),
        ],
        [
            InlineKeyboardButton(text=_["PL_B_4"], callback_data="PM"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def top_play_markup(_):
    return [
        [InlineKeyboardButton(text=_["PL_B_9"], callback_data="SERVERTOP global")],
        [InlineKeyboardButton(text=_["PL_B_10"], callback_data="SERVERTOP chat")],
        [InlineKeyboardButton(text=_["PL_B_11"], callback_data="SERVERTOP user")],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="get_playmarkup"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def get_playlist_markup(_):
    return [
        [
            InlineKeyboardButton(text=_["P_B_1"], callback_data="play_playlist a"),
            InlineKeyboardButton(text=_["P_B_2"], callback_data="play_playlist b"),
        ],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="home_play"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def top_play_markup(_):
    return [
        [InlineKeyboardButton(text=_["PL_B_9"], callback_data="SERVERTOP Global")],
        [InlineKeyboardButton(text=_["PL_B_10"], callback_data="SERVERTOP Group")],
        [InlineKeyboardButton(text=_["PL_B_11"], callback_data="SERVERTOP Personal")],
        [
            InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="get_playmarkup"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def failed_top_markup(_):
    return [
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]


def warning_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["PL_B_7"],
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def close_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
