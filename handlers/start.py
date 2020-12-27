from pyrogram import filters
from pyrogram.handlers import MessageHandler


async def start(client, message):
    await message.reply_text("سلام دوست عزیز🤩،به ربات پخش موزیک در ویس چت خوش اومدی ! میتونی لینک موزیکی که از یوتیوب داری رو برام بفرستی تا برات توی ویس چت پخش کنم برای فرستادن راحت تر لینک از @vid استفاده کنید.😊")
__handlers__ = [
    [
        MessageHandler(
            start,
            filters.command("start", "/")
            & filters.private
        )
    ]
]
