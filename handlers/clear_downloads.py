import os
from pyrogram import filters
from pyrogram.handlers import MessageHandler
import player
from config import SUDO_FILTER


async def clear_downloads(client, message):
    player.abort()
    try:
        for file in os.listdir("downloads"):
            try:
                os.remove("downloads/" + file)
            except:
                pass
        await message.reply_text("تمامی فایل های دانلود شده در سرور پاک شدند.")
    except:
        await message.reply_text("پاک نشد! شاید پوشه دانلودها خالیه!")

__handlers__ = [
    [
        MessageHandler(
            clear_downloads,
            filters.command("cdw", "/")
            & SUDO_FILTER
        )
    ]
]
