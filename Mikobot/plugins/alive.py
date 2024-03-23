# SOURCE https://github.com/Team-ProjectCodeX
# CREATED BY https://t.me/hasnainkk
# PROVIDED BY https://t.me/ProjectCodeX

# <============================================== IMPORTS =========================================================>
import random
from sys import version_info

import pyrogram
import telegram
import telethon
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from Infamous.karma import ALIVE_ANIMATION, ALIVE_BTN
from Mikobot import BOT_NAME, app

# <=======================================================================================================>


# <================================================ FUNCTION =======================================================>
@app.on_message(filters.command("alive"))
async def alive(_, message: Message):
    library_versions = {
      » *"ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ": telegram.__version__,
      » *"ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ": telethon.__version__,
       » *"ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ": pyrogram.__version__,
    }

    library_versions_text = "\n".join(
        [f"➲ **{key}:** `{value}`" for key, value in library_versions.items()]
    )

    caption = f"""**ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}**

     ━━━━━━━━ 🝮✿🝮 ━━━━━━━━
 **♛ ᴅᴇᴠᴏᴛᴇᴅ ᴛᴏ:** [Hasnain khan](https://t.me/hasnainkk)

{library_versions_text}

» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ:** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
» ** ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ:** `2.0`
     ━━━━━━━━ 🝮✿🝮 ━━━━━━━━"""

    await message.reply_animation(
        random.choice(ALIVE_ANIMATION),
        caption=caption,
        reply_markup=InlineKeyboardMarkup(ALIVE_BTN),
    )


# <=======================================================================================================>


# <================================================ NAME =======================================================>
__mod_name__ = "ALIVE"
# <================================================ END =======================================================>
