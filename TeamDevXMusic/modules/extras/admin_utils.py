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

import datetime as dt
import re
from typing import Optional, Tuple

from pyrogram import filters, enums
from pyrogram.errors import UserNotParticipant, RPCError
from pyrogram.types import Message


def mention(user_id: int, name: str) -> str:
    safe = name.replace("<", "&lt;").replace(">", "&gt;")
    return f'<a href="tg://user?id={user_id}">{safe}</a>'

_TIME_RE = re.compile(r"^(\d+)([smhd])$", re.IGNORECASE)
_UNITS = {"s": 1, "m": 60, "h": 3600, "d": 86400}


def parse_time(raw: str) -> Optional[dt.timedelta]:
    m = _TIME_RE.match(raw.strip())
    if not m:
        return None
    value, unit = int(m.group(1)), m.group(2).lower()
    return dt.timedelta(seconds=value * _UNITS[unit])

async def extract_user_and_reason(
    message: Message, client
) -> Tuple[Optional[int], str, Optional[str]]:
    args = message.command[1:]

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        reason = " ".join(args) if args else None
        return user.id, user.first_name, reason

    if args:
        target = args[0]
        reason = " ".join(args[1:]) or None
        try:
            user = await client.get_users(target)
            return user.id, user.first_name, reason
        except Exception:
            await message.reply_text(f"» Cannot find user: <code>{target}</code>")
            return None, "", None

    return None, "", None


async def extract_user_and_title(
    message: Message, client
) -> Tuple[Optional[int], str, Optional[str]]:
    args = message.command[1:]

    if message.reply_to_message and message.reply_to_message.from_user:
        user = message.reply_to_message.from_user
        title = args[0] if args else None
        return user.id, user.first_name, title

    if args:
        target = args[0]
        title = args[1] if len(args) > 1 else None
        try:
            user = await client.get_users(target)
            return user.id, user.first_name, title
        except Exception:
            await message.reply_text(f"» Cannot find user: <code>{target}</code>")
            return None, "", None

    return None, "", None

def admin_required(*permissions: str):
    def decorator(func):
        async def wrapper(client, message: Message):
            if message.chat.type == enums.ChatType.PRIVATE:
                return await func(client, message)

            invoker = message.from_user
            if not invoker:
                return

            try:
                member = await client.get_chat_member(message.chat.id, invoker.id)
            except (UserNotParticipant, RPCError):
                return await message.reply_text("» I can't fetch your member info.")

            status = member.status
            if status == enums.ChatMemberStatus.OWNER:
                return await func(client, message)

            if status != enums.ChatMemberStatus.ADMINISTRATOR:
                return await message.reply_text("» You need to be an admin to use this command.")

            for perm in permissions:
                if not getattr(member.privileges, perm, False):
                    return await message.reply_text(
                        f"» You don't have the <b>{perm}</b> permission."
                    )

            return await func(client, message)

        wrapper.__name__ = func.__name__
        return wrapper

    return decorator


async def _is_admin(client, chat_id: int, user_id: int) -> bool:
    try:
        member = await client.get_chat_member(chat_id, user_id)
        return member.status in (
            enums.ChatMemberStatus.ADMINISTRATOR,
            enums.ChatMemberStatus.OWNER,
        )
    except Exception:
        return False


async def _admin_filter_func(_, client, message: Message) -> bool:
    if not message.from_user:
        return False
    return await _is_admin(client, message.chat.id, message.from_user.id)

admin_filter = filters.create(_admin_filter_func)


async def is_admin(client, message: Message) -> bool:
    if not message.from_user:
        return False
    return await _is_admin(client, message.chat.id, message.from_user.id)


async def is_owner_or_sudoer(client, message: Message) -> bool:
    from config import OWNER_ID
    if message.from_user and message.from_user.id == OWNER_ID:
        return True
    try:
        member = await client.get_chat_member(message.chat.id, message.from_user.id)
        return member.status == enums.ChatMemberStatus.OWNER
    except Exception:
        return False
