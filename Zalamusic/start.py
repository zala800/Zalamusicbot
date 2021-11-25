from pyrogram import Client as Aliciabot, filters
from pyrogram.types import Message, InlineKeyboardMarkup, l
from Zalamusic.config import BOT_NAME as bn, BOT_USERNAME as bu, ASSISTANT_NAME as an, SUPPORT_GROUP as sg, BG_IMAGE as bi, OWNER

@Aliciabot.on_message(filters.command(["start"]) & filters.private & ~filters.edited)
async def start_(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}![🤓]({bi})
        
I am {bn}
I can play songs in your group's VC 🤗
To listen songs add me to your group..
And don't forgot to promote me with all rights!🥰
Otherwise I can't play songs!🥺👉👈
Use the buttons below to know more about me..😊
Add My Assistant @{an}
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "⚡Commands⚡", url="https://telegra.ph/MUSIC-BOT-COMMANDS-09-28")
                  ],[
                    InlineKeyboardButton(
                        "Owner👑", url="https://t.me/{OWNER}"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Group", url="https://t.me/{sg}"
                    )],[
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/{bu}?startgroup=true"
                    )
                ]
            ]
        ),
    )

@Aliciabot.on_message(filters.command(["start"] & filters.private & ~filters.edited))
async def gstart(client: Aliciabot, message: Message):
      await message.reply_text("""**{bn} is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Owner👑", url="https://t.me/{OWNER}")
                ]
            ]
        )
   )


@Aliciabot.on_message(filters.command(["help"]) & filters.private & ~filters.edited)
async def help(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
        message.from_user.mention)}! [Click here](https://telegra.ph/MUSIC-BOT-COMMANDS-09-28) to know about my Commands.⚡🔥
        """)
        

@Aliciabot.on_message(filters.command(["commands"]) & filters.private & ~filters.channel)
async def commands(client: Aliciabot, message: Message):
    await message.reply_text(
        f"""<b>Hey there {format(
          message.from_user.mention)}! [Click here](https://telegra.ph/MUSIC-BOT-COMMANDS-09-28) to know about my Commands.⚡🔥
        """)
