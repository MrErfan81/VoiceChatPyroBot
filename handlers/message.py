from pyrogram import filters
from pyrogram.handlers import MessageHandler
from helpers import is_youtube
from ytdl import download
import player
from config import LOG_GROUP


async def message(client, message):
    if message.text.startswith("/"):
        return

    if not is_youtube(message.text):
        await message.reply_text("❌لینک داده شده مشکل داره دوباره بفرست")
        return

    if "list=" in message.text:
        await message.reply_text("یه لینک موزیک ویدیو بفرست نه یک پلی لیست!🤨")
        return

    await message.reply_text("موزیک در صف دانلوده صبر کن👀", quote=True)
    download(
        (
            message.reply_text,
            ("موزیکی که دادی داره دانلود میشه😉",)
        ),
        (
            message.reply_text,
            (f"دانلود شد و آهنگ شما بعد {player.q.qsize() + 1} آهنگ پخش میشه🥴🤩.",)
        ),
        [
            player.play,
            [
                None,
                (
                    message.reply_text,
                                        ("این موزیک الان داره توی ویس چت پخش میشه🤩🎧",)
                ),
                (
                   message.reply_text,
                    ("موزیک به اتمام رسید😊❤️",)
                ),
                None,
                None,
                message.from_user.id,
                message.from_user.first_name,
                [
                   client.send_message,
                    [
                        LOG_GROUP,
                        "<b>هم اکنون داره در ویس چت پخش میشه🤩🎧</b>\n"
                        "موزیک🎼: <a href=\"{}\">{}</a>\n"
                        "درخواست شده توسط😁: <a href=\"tg://user?id={}\">{}</a>"
                    ]
                ] if LOG_GROUP else None
            ]
        ],
        (
            message.reply_text,
            "نمیتونی که ویدیو های استریم (پخش زنده) رو پخش کنی!"
        ),
        message.text,
    )
    

__handlers__ = [
    [
        MessageHandler(
            message,
            filters.text
            & filters.private
            & ~ filters.regex(r"^x .+")
        ),
        2
    ]
]
