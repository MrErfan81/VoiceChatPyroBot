from pyrogram import filters
from pyrogram.handlers import MessageHandler
import player
from config import SUDO_FILTER


async def skip(client, message):
    if player.abort():
        await message.reply_text("خب الان موزیک قطع شد یا موزیک بعدی داره پلی میشه")
    else:
        await message.reply_text("هیچ موزیکی نیست که متوقفش کنم یا بزنم بعدی!")

__handlers__ = [
    [
        MessageHandler(
            skip,
            filters.command("skip", "/")
            & SUDO_FILTER
        )
    ]
]
