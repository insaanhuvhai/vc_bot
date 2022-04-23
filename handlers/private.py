import os

import youtube_dl
from youtube_search import YoutubeSearch
import requests

from helpers.filters import command, other_filters2, other_filters
from helpers.decorators import errors

from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Voice

from config import BOT_NAME as bn, PLAY_PIC


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    hell_pic = https://te.legra.ph/file/2e9b860dfd7e1e0244b43.jpg
    hell = f"━━━━━━━━━━━━━━━━━━
 ʜᴇya !
      ɪ ᴀᴍ ᴀᴋɪʀᴀ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ, ᴀ ʟᴀɢ ғʀᴇᴇ ᴍᴜsɪᴄ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘs ᴛᴏ  ᴘʟᴀʏ sᴏɴɢs ᴡɪᴛʜᴏᴜᴛ ᴇʀʀᴏʀ ᴀɴᴅ ʟᴀɢ. ᴀᴋɪʀᴀ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ɢɪᴠᴇs ʏᴏᴜ ᴇᴠᴇʀʏᴛʜɪɴɢ ʏᴏᴜ ʀᴇǫᴜɪʀᴇᴅ ᴀᴛ ʏᴏᴜʀ ᴘʟᴀᴄᴇ. ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ... 
  ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ...ᴀɴᴅ ɢɪᴠᴇ ᴍᴇ ᴄᴏᴍᴍᴀɴᴅs...  ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛᴇᴅ sᴏɴɢ ᴡɪᴛʜ ᴀ ɢᴀᴘ ᴏғ sᴇᴄᴏɴᴅs...  
   
      *ɴᴏᴛᴇ*- ᴅᴏɴ'ᴛ ғᴏʀɢᴇᴛ ᴛᴏ ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 😌.


━━━━━━━━━━━━━━━━━━"
    butts = InlineKeyboardMarkup(
        [  
                [
                    InlineKeyboardButton(
                        " ➕ Add me To Your Group ➕", url=f"https://t.me/Akira_MusicBot?startgroup=true"
                       ),
                    InlineKeyboardButton(
                    "Akira Official", url="https://t.meAkiraUpdates/"
                      ),
                      InlineKeyboardButton(
                    "Dev", url="https://t.me/AkHiL_SI"
                )
            ]
        ]
    )
    await message.reply_photo(
    photo=hell_pic,
    reply_markup=butts,
    caption=hell,
)



@Client.on_message(command("ping") & other_filters)
async def ping(_, message: Message):
    hell_pic = PLAY_PIC
    await message.reply_photo(
    photo=hell_pic,
    caption="I'm Alive and working fine. Do /help to get commands.\n\nHappy Streaming Music 😉",


@Client.on_message(command("song") & other_filters2)
@errors
async def a(client, message: Message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    okvai = query.capitalize()
    print(query.capitalize())
    m = await message.reply(f"**{bn} :-**  Searching for {okvai}")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            m.edit(f"**{bn} :-** 😕 Found nothing. Try changing the spelling a little.\n\n{e}")
            return
    except Exception as e:
        m.edit(
           f"**{bn} :-** 😕 Found Nothing. Sorry.\n\nTry another keywork or maybe spell it properly."
        )
        print(str(e))
        return
    await m.edit(f"**{bn} :-** 📥 Downloading...\n**Query :-** {okvai}")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎶 **Title:** [{title[:35]}]({link})\n⏳ **Duration:** {duration}\n'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        await  message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name)
        await m.delete()
    except Exception as e:
        m.edit(f"❌ Error!! \n\n{e}")
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
