import html
import json
import os
from typing import Optional

from telegram import Message, MessageEntity
from telegram.error import BadRequest
from telegram.ext import ContextTypes

from Mikobot import (
    DEMONS,
    DEV_USERS,
    DRAGONS,
    OWNER_ID,
    SUPPORT_CHAT,
    TIGERS,
    WOLVES,
    dispatcher,
)
from Mikobot.plugins.helper_funcs.chat_status import (
    dev_plus,
    sudo_plus,
    whitelist_plus,
)
from Mikobot.plugins.helper_funcs.extraction import extract_user
from Mikobot.plugins.log_channel import gloggable

ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "Mikobot/elevated_users.json")

def check_user_id(user_id: int, context: ContextTypes) -> Optional[str]:
    bot = context.bot
    if not user_id:
        reply = "That...is a chat! baka ka omae?"

    elif user_id == bot.id:
        reply = "This does not work that way."

    else:
        reply = None
    return reply


@dev_plus
@gloggable
def addsudo(context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        message.reply_text("This member is already a Dragon Disaster")
        return ""

    if user_id in DEMONS:
        rt += "Requested HA to promote a Demon Disaster to Dragon."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "Requested HA to promote a Wolf Disaster to Dragon."
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["sudos"].append(user_id)
    DRAGONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt
        + "\nSuccessfully set Disaster level of {} to Dragon!".format(
            user_member.first_name
        )
    )

    log_message = (
        f"#SUDO\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message


@sudo_plus
@gloggable
def addsupport(
    context: ContextTypes.DEFAULT_TYPE
) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "Requested HA to demote this Dragon to Demon"
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        message.reply_text("This user is already a Demon Disaster.")
        return ""

    if user_id in WOLVES:
        rt += "Requested HA to promote this Wolf Disaster to Demon"
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    data["supports"].append(user_id)
    DEMONS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\n{user_member.first_name} was added as a Demon Disaster!"
    )

    log_message = (
        f"#SUPPORT\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message


@sudo_plus
@gloggable
def addwhitelist(context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "This member is a Dragon Disaster, Demoting to Wolf."
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "This user is already a Demon Disaster, Demoting to Wolf."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        message.reply_text("This user is already a Wolf Disaster.")
        return ""

    data["whitelists"].append(user_id)
    WOLVES.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\nSuccessfully promoted {user_member.first_name} to a Wolf Disaster!"
    )

    log_message = (
        f"#WHITELIST\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message


@sudo_plus
@gloggable
def addtiger(context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)
    rt = ""

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        rt += "This member is a Dragon Disaster, Demoting to Tiger."
        data["sudos"].remove(user_id)
        DRAGONS.remove(user_id)

    if user_id in DEMONS:
        rt += "This user is already a Demon Disaster, Demoting to Tiger."
        data["supports"].remove(user_id)
        DEMONS.remove(user_id)

    if user_id in WOLVES:
        rt += "This user is already a Wolf Disaster, Demoting to Tiger."
        data["whitelists"].remove(user_id)
        WOLVES.remove(user_id)

    if user_id in TIGERS:
        message.reply_text("This user is already a Tiger.")
        return ""

    data["tigers"].append(user_id)
    TIGERS.append(user_id)

    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)

    update.effective_message.reply_text(
        rt + f"\nSuccessfully promoted {user_member.first_name} to a Tiger Disaster!"
    )

    log_message = (
        f"#TIGER\n"
        f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))} \n"
        f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
    )

    if chat.type != "private":
        log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

    return log_message


@dev_plus
@gloggable
def removesudo(context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DRAGONS:
        message.reply_text("Requested HA to demote this user to Civilian")
        DRAGONS.remove(user_id)
        data["sudos"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNSUDO\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = "<b>{}:</b>\n".format(html.escape(chat.title)) + log_message

        return log_message

    else:
        message.reply_text("This user is not a Dragon Disaster!")
        return ""


@sudo_plus
@gloggable
def removesupport(context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in DEMONS:
        message.reply_text("Requested HA to demote this user to Civilian")
        DEMONS.remove(user_id)
        data["supports"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNSUPPORT\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message

    else:
        message.reply_text("This user is not a Demon level Disaster!")
        return ""


@sudo_plus
@gloggable
def removewhitelist(context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in WOLVES:
        message.reply_text("Demoting to normal user")
        WOLVES.remove(user_id)
        data["whitelists"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNWHITELIST\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("This user is not a Wolf Disaster!")
        return ""


@sudo_plus
@gloggable
def removetiger(context: ContextTypes.DEFAULT_TYPE) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    user_id = extract_user(message, args)
    user_member = bot.getChat(user_id)

    reply = check_user_id(user_id, bot)
    if reply:
        message.reply_text(reply)
        return ""

    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)

    if user_id in TIGERS:
        message.reply_text("Demoting to normal user")
        TIGERS.remove(user_id)
        data["tigers"].remove(user_id)

        with open(ELEVATED_USERS_FILE, "w") as outfile:
            json.dump(data, outfile, indent=4)

        log_message = (
            f"#UNTIGER\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"<b>User:</b> {mention_html(user_member.id, html.escape(user_member.first_name))}"
        )

        if chat.type != "private":
            log_message = f"<b>{html.escape(chat.title)}:</b>\n" + log_message

        return log_message
    else:
        message.reply_text("This user is not a Tiger Disaster!")
        return ""


@whitelist_plus
def whitelistlist(context: ContextTypes.DEFAULT_TYPE):
    reply = "<b>Known Wolf Disasters 🐺:</b>\n"
    m = update.effective_message.reply_text(
        "<code>..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in WOLVES:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)

            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def tigerlist(context: ContextTypes.DEFAULT_TYPE):
    reply = "<b>ᴋɴᴏᴡɴ ᴛɪɢᴇʀ ᴅɪsᴀsᴛᴇʀs 🐯:</b>\n"
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    bot = context.bot
    for each_user in TIGERS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def supportlist(context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    reply = "<b> ᴋɴᴏᴡɴ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀs👹:</b>\n"
    for each_user in DEMONS:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def sudolist(context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>Gathering intel..</code>", parse_mode=ParseMode.HTML
    )
    true_sudo = list(set(DRAGONS)- set(DEV_USERS))
    reply = "<b> ᴋɴᴏᴡɴ ᴅʀᴀɢᴏɴ ᴅɪsᴀsᴛᴇʀs🐉:</b>\n"
    for each_user in true_sudo:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


@whitelist_plus
def devlist(context: ContextTypes.DEFAULT_TYPE):
    bot = context.bot
    m = update.effective_message.reply_text(
        "<code>ɢᴀᴛʜᴇʀɪɴɢ..</code>", parse_mode=ParseMode.HTML
    )
    true_dev = list(set(DEV_USERS) -{OWNER_ID})
    reply = "✨ <b>ᴅᴇᴠs ᴜsᴇʀ ʟɪsᴛ :</b>\n"
    for each_user in true_dev:
        user_id = int(each_user)
        try:
            user = bot.get_chat(user_id)
            reply += f"• {mention_html(user_id, html.escape(user.first_name))}\n"
        except TelegramError:
            pass
    m.edit_text(reply, parse_mode=ParseMode.HTML)


__help__ = f"""
*⚠️ ɴᴏᴛɪᴄᴇ:*
ᴄᴏᴍᴍᴀɴᴅs ʟɪsᴛᴇᴅ ʜᴇʀᴇ ᴏɴʟʏ ᴡᴏʀᴋ ғᴏʀ ᴜsᴇʀs ᴡɪᴛʜ sᴘᴇᴄɪᴀʟ ᴀᴄᴄᴇss ᴀʀᴇ ᴍᴀɪɴʟʏ ᴜsᴇᴅ ғᴏʀ ᴛʀᴏᴜʙʟᴇsʜᴏᴏᴛɪɴɢ, ᴅᴇʙᴜɢɢɪɴɢ ᴘᴜʀᴘᴏsᴇs.
ɢʀᴏᴜᴘ ᴀᴅᴍɪɴs/ɢʀᴏᴜᴘ ᴏᴡɴᴇʀs ᴅᴏ ɴᴏᴛ ɴᴇᴇᴅ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs. 

*ʟɪsᴛ ᴀʟʟ sᴘᴇᴄɪᴀʟ ᴜsᴇʀs:*
 ❍ /sudolist*:* ʟɪsᴛs ᴀʟʟ ᴅʀᴀɢᴏɴ ᴅɪsᴀsᴛᴇʀs
 ❍ /supportlist *:* ʟɪsᴛs ᴀʟʟ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀs
 ❍ /tigers *:* ʟɪsᴛs ᴀʟʟ ᴛɪɢᴇʀs ᴅɪsᴀsᴛᴇʀs
 ❍ /wolves *:* ʟɪsᴛs ᴀʟʟ ᴡᴏʟғ ᴅɪsᴀsᴛᴇʀs
 ❍ /devlist *:* ʟɪsᴛs ᴀʟʟ ʜᴇʀᴏ ᴀssᴏᴄɪᴀᴛɪᴏɴ ᴍᴇᴍʙᴇʀs
 ❍ /addsudo  *:* ᴀᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ ᴅʀᴀɢᴏɴ
 ❍ /adddemon *:* ᴀᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ ᴅᴇᴍᴏɴ
 ❍ /addtiger *:* ᴀᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ ᴛɪɢᴇʀ
 ❍ /addwolf*:* ᴀᴅᴅs ᴀ ᴜsᴇʀ ᴛᴏ ᴡᴏʟғ
 ❍ `ᴀᴅᴅ ᴅᴇᴠ ᴅᴏᴇsɴᴛ ᴇxɪsᴛ, ᴅᴇᴠs sʜᴏᴜʟᴅ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴀᴅᴅ ᴛʜᴇᴍsᴇʟᴠᴇs`

*ᴘɪɴɢ:*
 ❍ /ping *:* ɢᴇᴛs ᴘɪɴɢ ᴛɪᴍᴇ ᴏғ ʙᴏᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ sᴇʀᴠᴇʀ

*ʙʀᴏᴀᴅᴄᴀsᴛ: (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)*
*ɴᴏᴛᴇ:* ᴛʜɪs sᴜᴘᴘᴏʀᴛs ʙᴀsɪᴄ ᴍᴀʀᴋᴅᴏᴡɴ
 ❍ /broadcastall *:* ʙʀᴏᴀᴅᴄᴀsᴛs ᴇᴠᴇʀʏᴡʜᴇʀᴇ
 ❍ broadcastusers *:* ʙʀᴏᴀᴅᴄᴀsᴛs ᴛᴏᴏ ᴀʟʟ ᴜsᴇʀs
 ❍ /broadcastgroups *:* ʙʀᴏᴀᴅᴄᴀsᴛs ᴛᴏᴏ ᴀʟʟ ɢʀᴏᴜᴘs



`⚠️ ʀᴇᴀᴅ ғʀᴏᴍ ᴛᴏᴘ`
ᴠɪsɪᴛ [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]("https://t.me{SUPPORT_CHAT}") ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
"""

SUDO_HANDLER = "addsudo"
SUPPORT_HANDLER = "addsupport", "adddemon"
TIGER_HANDLER = "addtiger"
WHITELIST_HANDLER = "addwhitelist", "addwolf"
UNSUDO_HANDLER = "removesudo", "rmsudo"
UNSUPPORT_HANDLER = "removesupport", "removedemon"
UNTIGER_HANDLER = "removetiger"
UNWHITELIST_HANDLER = "removewhitelist", "removewolf"
WHITELISTLIST_HANDLER = "whitelistlist", "wolves"
TIGERLIST_HANDLER = "tigers"
SUPPORTLIST_HANDLER = "supportlist"
SUDOLIST_HANDLER = "sudolist"
DEVLIST_HANDLER = "devlist"

dispatcher.add.handler(SUDO_HANDLER)
dispatcher.add.handler(SUPPORT_HANDLER)
dispatcher.add_handler(TIGER_HANDLER)
dispatcher.add_handler(WHITELIST_HANDLER)
dispatcher.add_handler(UNSUDO_HANDLER)
dispatcher.add_handler(UNSUPPORT_HANDLER)
dispatcher.add_handler(UNTIGER_HANDLER)
dispatcher.add_handler(UNWHITELIST_HANDLER)
dispatcher.add_handler(WHITELISTLIST_HANDLER)
dispatcher.add_handler(TIGERLIST_HANDLER)
dispatcher.add_handler(SUPPORTLIST_HANDLER)
dispatcher.add_handler(SUDOLIST_HANDLER)
dispatcher.add_handler(DEVLIST_HANDLER)

__mod_name__ = "DEVS"
__handlers__ = [
    SUDO_HANDLER,
    SUPPORT_HANDLER,
    TIGER_HANDLER,
    WHITELIST_HANDLER,
    UNSUDO_HANDLER,
    UNSUPPORT_HANDLER,
    UNTIGER_HANDLER,
    UNWHITELIST_HANDLER,
    WHITELISTLIST_HANDLER, 
    TIGERLIST_HANDLER,
    SUPPORTLIST_HANDLER,
    SUDOLIST_HANDLER,
    DEVLIST_HANDLER,
]
