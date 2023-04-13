from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN
from AniPlay.plugins.stats import day, over

from database.database import full_userbase

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from config import MUST_JOIN, ADMINS


@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"**ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ iɴ ᴍʏ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ ᴛᴏ ᴜsᴇ ᴍᴇ\n\n ᴋɪɴᴅʟʏ ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ🍁**",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ᴊᴏɪɴ", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in {MUST_JOIN} !")



@app.on_message(filters.command(['start', 'ping', 'help', 'alive']))
async def start(_, message: Message):
    try:
        await message.reply_text('ʙᴏᴛ ɪs ᴏɴʟɪɴᴇ , \nʏᴏᴜ ᴄᴀɴ ᴡᴀᴛᴄʜ ᴀɴɪᴍᴇ ᴏɴʟɪɴᴇ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴘ ᴏғ ᴛʜᴇ ʙᴏᴛ \nᴇx- /search Anime name or /s Anime name\n\nɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ᴛʜᴇɴ ᴄᴏɴᴛᴀᴄᴛ @The_Nanamii\n\nᴊᴏɪɴ ғᴏʀ ᴍᴏʀᴇ ʙᴏᴛs : @Campus_Bot_Updates')
    except:
        return


@app.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def _stats(_, msg: Message):
    users = await full_userbase()
    await msg.reply(f"{len(users)} users are using this bot")


QUERY = '**Search Results:** `{}`'


@app.on_message(filters.command(['search', 's']))
async def searchCMD(_, message: Message):
    try:
        user = message.from_user.id
        query = ' '.join(message.command[1:])
        if query == '':
            return await message.reply_text('Give me something to search ^_^')
        data = AnimeDex.search(query)
        button = BTN.searchCMD(user, data, query)
        await message.reply_text(QUERY.format(query), reply_markup=button)
    except Exception as e:
        try:
            return await message.reply_text('**Anime Not Found...**\n\nProbably Incorrect Name, Try again')
        except:
            return


@app.on_message(filters.command('stats'))
async def stats(_, message: Message):
    try:
        await message.reply_text('Use /stats1 For Day Wise Stats\nAnd /stats2 For Overall Stats')
    except:
        return


@app.on_message(filters.command('stats1'))
async def stats1(_, message: Message):
    try:
        img = day()
        await message.reply_photo(img, caption='**AnimeDex | Day Wise Stats**')
    except:
        return


@app.on_message(filters.command('stats2'))
async def stats2(_, message: Message):
    try:
        img = over()
        await message.reply_photo(img, caption='**AnimeDex | Overall Stats**')
    except:
        return
