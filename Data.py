from pyrogram.types import InlineKeyboardButton


class Data:
    START = """
Hello {}

ɪғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴛʀᴜsᴛ ᴛʜɪs ʙᴏᴛ:

#ᴘʟᴇᴀsᴇ sᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪs ᴍᴇssᴀɢᴇ ᴅᴇʟᴇᴛᴇ ᴛʜɪs ᴄʜᴀᴛ

ᴛʜɪs ʙᴏᴛ ʜᴇʟᴘs ʏᴏᴜ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴs.
ғᴏʀ sᴀғᴇᴛʏ, ᴀʟᴡᴀʏs ᴜsᴇ ᴀ sᴇᴄᴏɴᴅᴀʀʏ ᴀᴄᴄᴏᴜɴᴛ.

ᴍᴀɴᴀɢᴇᴅ ʙʏ - @TwsAssociation
    """

    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton(text="ʜᴏᴍᴇ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")]
    ]

    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴇssɪᴏɴ", callback_data="generate")],
        [InlineKeyboardButton("ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ", url="https://t.me/TwsAssociation")],
        [
            InlineKeyboardButton("ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/TwsAssociation")]
    ]

    HELP = """
✨ **ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs** ✨

/about - ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ
/help - ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ
/start - sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
/generate - sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ᴀ sᴇssɪᴏɴ
/cancel - ᴄᴀɴᴄᴇʟ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʀᴏᴄᴇss
/restart - ʀᴇsᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ
"""

    ABOUT = """
🌟 **ᴀʙᴏᴜᴛ ᴛʜɪs ʙᴏᴛ** 🌟

ᴛʜɪs ɪs ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ **ᴘʏʀᴏɢʀᴀᴍ** ᴀɴᴅ **ᴛᴇʟᴇᴛʜᴏɴ** sᴛʀɪɴɢ sᴇssɪᴏɴs.

🔧 **ғʀᴀᴍᴇᴡᴏʀᴋ:** https://docs.kurigram.icu/  
🐍 **ʟᴀɴɢᴜᴀɢᴇ:** https://www.python.org/  
🛠 **ᴘᴜʀᴘᴏsᴇ:** ɢᴇɴᴇʀᴀᴛᴇ sᴀғᴇ sᴇssɪᴏɴ sᴛʀɪɴɢs ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʟɪᴇɴᴛs  

📢 **ᴜᴘᴅᴀᴛᴇs:** https://t.me/TwsAssociation  
👤 **ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ:** @TwsAssociation
    """
