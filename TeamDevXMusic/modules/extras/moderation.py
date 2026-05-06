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
import datetime as dt
from typing import Optional

from pyrogram import filters, enums
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid, UserNotParticipant, RPCError
from pyrogram.types import ChatPermissions, Message

from config import BANNED_USERS
from TeamDevXMusic import app
from TeamDevXMusic.modules.extras.admin_utils import (
    admin_required,
    extract_user_and_reason,
    mention,
    parse_time,
)


TEAMDEV = "TeamDev"
MR_D = "mr_d"
TEAM_X_OG = "team_x_og"

_MUTE_PERMS = ChatPermissions()

_USAGES = {
    "ban":    "/ban @user [reason] — or reply with /ban [reason]",
    "unban":  "/unban @user — or reply with /unban",
    "mute":   "/mute @user [reason] — or reply with /mute [reason]",
    "unmute": "/unmute @user — or reply with /unmute",
    "tmute":  "/tmute @user <time> [reason] e.g. /tmute @user 1h reason",
    "kick":   "/kick @user [reason] — or reply with /kick [reason]",
    "dban":   "Reply to a message with /dban [reason]",
    "sban":   "/sban @user — or reply with /sban",
    "tban":   "/tban @user <time> [reason] e.g. /tban @user 1d reason",
    "kickme": "/kickme — kick yourself from the group",
}


async def _get_member(client, chat_id: int, user_id: int):
    try:
        return await client.get_chat_member(chat_id, user_id)
    except (UserNotParticipant, RPCError):
        return None


def _is_admin(status: enums.ChatMemberStatus) -> bool:
    return status in (enums.ChatMemberStatus.ADMINISTRATOR, enums.ChatMemberStatus.OWNER)


def TeamDev_success_text(action: str, msg: Message, uid: int, name: str, reason: Optional[str]) -> str:
    user_m = mention(uid, name)
    admin_m = mention(msg.from_user.id, msg.from_user.first_name)
    text = (
        f"» {action} ᴀ ᴜsᴇʀ ɪɴ {msg.chat.title}\n"
        f" ᴜsᴇʀ  : {user_m}\n"
        f" ᴀᴅᴍɪɴ : {admin_m}"
    )
    if reason:
        text += f"\n» Reason: {reason}"
    return text


@app.on_message(filters.command("ban") & ~BANNED_USERS)
@admin_required("can_restrict_members")
async def mr_d_ban(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_USAGES["ban"])

    uid, name, reason = await extract_user_and_reason(message, client)
    if not uid:
        return

    target = await _get_member(client, message.chat.id, uid)
    if target and _is_admin(target.status):
        return await message.reply_text("» I cannot ban an admin or the group owner.")
    if target and target.status == enums.ChatMemberStatus.BANNED:
        return await message.reply_text("» User is already banned.")

    try:
        await client.ban_chat_member(message.chat.id, uid)
        await message.reply_text(TeamDev_success_text("Ban", message, uid, name, reason))
    except ChatAdminRequired:
        await message.reply_text("» I need ban permissions.")
    except UserAdminInvalid:
        await message.reply_text("» I cannot ban an admin.")


@app.on_message(filters.command("unban") & ~BANNED_USERS)
@admin_required("can_restrict_members")
async def team_x_og_unban(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_USAGES["unban"])

    uid, name, reason = await extract_user_and_reason(message, client)
    if not uid:
        return

    mem = await _get_member(client, message.chat.id, uid)
    if not mem or mem.status != enums.ChatMemberStatus.BANNED:
        return await message.reply_text("» User is not banned.")

    try:
        await client.unban_chat_member(message.chat.id, uid)
        await message.reply_text(TeamDev_success_text("Unban", message, uid, name, reason))
    except ChatAdminRequired:
        await message.reply_text("» I need unban permissions.")

@app.on_message(filters.command("mute") & ~BANNED_USERS)
@admin_required("can_restrict_members")
async def TeamDev_mute(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_USAGES["mute"])

    uid, name, reason = await extract_user_and_reason(message, client)
    if not uid:
        return

    target = await _get_member(client, message.chat.id, uid)
    if target and _is_admin(target.status):
        return await message.reply_text("» I cannot mute an admin or the group owner.")

    try:
        await client.restrict_chat_member(message.chat.id, uid, _MUTE_PERMS)
        await message.reply_text(TeamDev_success_text("Mute", message, uid, name, reason))
    except ChatAdminRequired:
        await message.reply_text("» I need mute permissions.")
    except UserAdminInvalid:
        await message.reply_text("» I cannot mute an admin.")

@app.on_message(filters.command("unmute") & ~BANNED_USERS)
@admin_required("can_restrict_members")
async def mr_d_unmute(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_USAGES["unmute"])

    uid, name, reason = await extract_user_and_reason(message, client)
    if not uid:
        return

    perms = ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_polls=True,
        can_send_other_messages=True,
        can_add_web_page_previews=True,
        can_invite_users=True,
    )
    try:
        await client.restrict_chat_member(message.chat.id, uid, perms)
        await message.reply_text(TeamDev_success_text("Unmute", message, uid, name, reason))
    except ChatAdminRequired:
        await message.reply_text("» I need unmute permissions.")


@app.on_message(filters.command("tmute") & ~BANNED_USERS)
@admin_required("can_restrict_members")
async def team_x_og_tmute(client, message: Message):
    if message.reply_to_message:
        if len(message.command) < 2:
            return await message.reply_text(_USAGES["tmute"])
        user = message.reply_to_message.from_user
        time_arg = message.command[1]
        reason = message.text.partition(time_arg)[2].strip() or None
    else:
        if len(message.command) < 3:
            return await message.reply_text(_USAGES["tmute"])
        user = await client.get_users(message.command[1])
        if not user:
            return await message.reply_text("» Can't find that user.")
        time_arg = message.command[2]
        reason = message.text.partition(time_arg)[2].strip() or None

    target = await _get_member(client, message.chat.id, user.id)
    if target and _is_admin(target.status):
        return await message.reply_text("» I cannot mute an admin or the group owner.")

    delta = parse_time(time_arg)
    if not delta:
        return await message.reply_text("» Invalid time format. Use 30s / 5m / 2h / 1d.")

    until = dt.datetime.now(dt.timezone.utc) + delta
    try:
        await client.restrict_chat_member(message.chat.id, user.id, _MUTE_PERMS, until_date=until)
        await message.reply_text(TeamDev_success_text(f"Temp Mute ({time_arg})", message, user.id, user.first_name, reason))
    except (ChatAdminRequired, UserAdminInvalid):
        await message.reply_text("» I need mute permissions / cannot mute an admin.")

@app.on_message(filters.command("kick") & ~BANNED_USERS)
@admin_required("can_restrict_members")
async def TeamDev_kick(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_USAGES["kick"])

    uid, name, reason = await extract_user_and_reason(message, client)
    if not uid:
        return

    target = await _get_member(client, message.chat.id, uid)
    if target and _is_admin(target.status):
        return await message.reply_text("» I cannot kick an admin or the group owner.")

    try:
        await client.ban_chat_member(message.chat.id, uid)
        await asyncio.sleep(2)
        await client.unban_chat_member(message.chat.id, uid)
        await message.reply_text(TeamDev_success_text("Kick", message, uid, name, reason))
    except ChatAdminRequired:
        await message.reply_text("» I need ban permissions.")
    except UserAdminInvalid:
        await message.reply_text("» I cannot kick an admin.")

@app.on_message(filters.command("dban") & ~BANNED_USERS)
@admin_required("can_restrict_members")
async def mr_d_dban(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text(_USAGES["dban"])

    user = message.reply_to_message.from_user
    reason = " ".join(message.command[1:]) or None

    target = await _get_member(client, message.chat.id, user.id)
    if target and _is_admin(target.status):
        return await message.reply_text("» I cannot ban an admin or the group owner.")

    try:
        await client.ban_chat_member(message.chat.id, user.id)
        await message.reply_to_message.delete()
        await message.reply_text(TeamDev_success_text("Ban", message, user.id, user.first_name, reason))
    except (ChatAdminRequired, UserAdminInvalid):
        await message.reply_text("» I need ban & delete permissions.")

@app.on_message(filters.command("sban") & ~BANNED_USERS)
@admin_required("can_restrict_members")
async def team_x_og_sban(client, message: Message):
    if len(message.command) == 1 and not message.reply_to_message:
        return await message.reply_text(_USAGES["sban"])

    uid, _, _ = await extract_user_and_reason(message, client)
    if not uid:
        return

    target = await _get_member(client, message.chat.id, uid)
    if target and _is_admin(target.status):
        return await message.reply_text("» I cannot ban an admin or the group owner.")

    try:
        await client.ban_chat_member(message.chat.id, uid)
        await message.delete()
    except ChatAdminRequired:
        await message.reply_text("» I need ban permissions.")
    except UserAdminInvalid:
        await message.reply_text("» I cannot ban an admin.")


@app.on_message(filters.command("kickme") & ~BANNED_USERS)
async def TeamDev_kickme(client, message: Message):
    if message.chat.type == enums.ChatType.PRIVATE:
        return

    target = await _get_member(client, message.chat.id, message.from_user.id)
    if target and _is_admin(target.status):
        return await message.reply_text("» Nice try, boss — I can't kick admins or the owner.")

    me = await _get_member(client, message.chat.id, (await client.get_me()).id)
    if not me or not getattr(me.privileges, "can_restrict_members", False):
        return await message.reply_text("» I need ban permissions to kick you.")

    try:
        await client.ban_chat_member(message.chat.id, message.from_user.id)
        await asyncio.sleep(3)
        await client.unban_chat_member(message.chat.id, message.from_user.id)
        await message.reply_text("» Kicked so hard, your ancestors felt it! »")
    except (ChatAdminRequired, UserAdminInvalid):
        await message.reply_text("» I can't kick admins or the owner.")


@app.on_message(filters.command("tban") & ~BANNED_USERS)
@admin_required("can_restrict_members")
async def mr_d_tban(client, message: Message):
    if message.reply_to_message:
        if len(message.command) < 2:
            return await message.reply_text(_USAGES["tban"])
        user = message.reply_to_message.from_user
        time_arg = message.command[1]
        reason = message.text.partition(time_arg)[2].strip() or None
    else:
        if len(message.command) < 3:
            return await message.reply_text(_USAGES["tban"])
        user = await client.get_users(message.command[1])
        if not user:
            return await message.reply_text("» Can't find that user.")
        time_arg = message.command[2]
        reason = message.text.partition(time_arg)[2].strip() or None

    target = await _get_member(client, message.chat.id, user.id)
    if target and _is_admin(target.status):
        return await message.reply_text("» I cannot ban an admin or the group owner.")

    delta = parse_time(time_arg)
    if not delta:
        return await message.reply_text("» Invalid time format. Use 30s / 5m / 2h / 1d.")

    until = dt.datetime.now(dt.timezone.utc) + delta
    try:
        await client.ban_chat_member(message.chat.id, user.id, until_date=until)
        await message.reply_text(TeamDev_success_text(f"Temp Ban ({time_arg})", message, user.id, user.first_name, reason))
    except (ChatAdminRequired, UserAdminInvalid):
        await message.reply_text("» I need ban permissions / cannot ban an admin.")
