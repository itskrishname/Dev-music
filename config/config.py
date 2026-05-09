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

import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

OWNER_ID = int(getenv("OWNER_ID", None))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/itskrishname/Dev-music")

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SECRECT_BOT_UPDATES")

SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/Lord_Vasudev_Krishna")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "False")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", "https://t.me/Lord_Vasudev_Krishna")

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "2"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "7"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))

COOKIES = getenv("COOKIES", None)

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "TeamDev.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/m36fkf.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

GLOBAL_IMG_URL = getenv(
    "GLOBAL_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

STATS_IMG_URL = getenv(
    "STATS_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)

SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL",
    "https://files.catbox.moe/m36fkf.jpg",
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    print(
        "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if SUPPORT_GROUP and not re.match("(?:http|https)://", SUPPORT_GROUP):
    print(
        "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if UPSTREAM_REPO and not re.match("(?:http|https)://", UPSTREAM_REPO):
    print(
        "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if GITHUB_REPO and not re.match("(?:http|https)://", GITHUB_REPO):
    print(
        "[ERROR] - Your GITHUB_REPO url is wrong. Please ensure that it starts with https://"
    )


if (
    PING_IMG_URL
    and PING_IMG_URL != "https://files.catbox.moe/m36fkf.jpg"
    and not re.match("(?:http|https)://", PING_IMG_URL)
):
    print(
        "[ERROR] - Your PING_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    PLAYLIST_IMG_URL
    and PLAYLIST_IMG_URL != "https://files.catbox.moe/m36fkf.jpg"
    and not re.match("(?:http|https)://", PLAYLIST_IMG_URL)
):
    print(
        "[ERROR] - Your PLAYLIST_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    GLOBAL_IMG_URL
    and GLOBAL_IMG_URL != "https://files.catbox.moe/m36fkf.jpg"
    and not re.match("(?:http|https)://", GLOBAL_IMG_URL)
):
    print(
        "[ERROR] - Your GLOBAL_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if STATS_IMG_URL and (
    STATS_IMG_URL != "https://files.catbox.moe/m36fkf.jpg"
    and not re.match("(?:http|https)://", STATS_IMG_URL)
):
    print(
        "[ERROR] - Your STATS_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    TELEGRAM_AUDIO_URL
    and TELEGRAM_AUDIO_URL != "https://files.catbox.moe/m36fkf.jpg"
    and not re.match("(?:http|https)://", TELEGRAM_AUDIO_URL)
):
    print(
        "[ERROR] - Your TELEGRAM_AUDIO_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    STREAM_IMG_URL
    and STREAM_IMG_URL != "https://files.catbox.moe/m36fkf.jpg"
    and not re.match("(?:http|https)://", STREAM_IMG_URL)
):
    print(
        "[ERROR] - Your STREAM_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    SOUNCLOUD_IMG_URL
    and SOUNCLOUD_IMG_URL != "https://files.catbox.moe/m36fkf.jpg"
    and not re.match("(?:http|https)://", SOUNCLOUD_IMG_URL)
):
    print(
        "[ERROR] - Your SOUNCLOUD_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()

if (
    YOUTUBE_IMG_URL
    and YOUTUBE_IMG_URL != "https://files.catbox.moe/m36fkf.jpg"
    and not re.match("(?:http|https)://", YOUTUBE_IMG_URL)
):
    print(
        "[ERROR] - Your YOUTUBE_IMG_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()


if (
    TELEGRAM_VIDEO_URL
    and TELEGRAM_VIDEO_URL != "https://files.catbox.moe/m36fkf.jpg"
    and not re.match("(?:http|https)://", TELEGRAM_VIDEO_URL)
):
    print(
        "[ERROR] - Your TELEGRAM_VIDEO_URL url is wrong. Please ensure that it starts with https://"
    )
    sys.exit()
