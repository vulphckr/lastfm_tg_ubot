import asyncio
import sys 

from pyrogram import Client, filters
from Scrobbler import Scrobbler

API_ID = 123456 # Insert your Telegram api_id here
API_HASH = "" # Insert your Telegram api_hash here
lastFm = Scrobbler()
bot = Client("your_name", api_id=API_ID, api_hash=API_HASH)
scrobblingStatus = False

# Clears all the audios on the profile
async def clearAudio():
    async for audio in bot.get_chat_audios("me"):
        await bot.remove_profile_audio(audio.file_id)

# Retrieves the current audio file id from the profile
async def retrieveCurrAudio():
    return await bot.get_chat_audios("me")[0].file_id

# Stops the bot
@bot.on_message(filters.command("stop", "-"), filters.me)
async def stopCommand(client, message):
    await client.edit_message_text(message.chat.id, message.id, "Bot stopped from -stop command.")
    await bot.add_profile_audio("file.mp3", title="⚠️ Bot Stopped")
    sys.exit()


# Command -scrobble to enable/disable scrobbling
@bot.on_message(filters.command("scrobble", "-"), filters.me)
async def profileScrobblingCommand(client, message):
    global scrobblingStatus
    if(scrobblingStatus is True):
        scrobblingStatus = False
        await client.edit_message_text(message.chat.id, message.id, "Scrobbling on profile disabled")
    else:
        scrobblingStatus = True
        await client.edit_message_text(message.chat.id, message.id, "Scrobbling on profile enabled")
        await profileScrobbler()

# Displays, on -np command, the current song w/ author. If nothing is playing displays a placeholder.
@bot.on_message(filters.command("np", "-"), filters.me)
async def nowPlayingCommand(client, message):
    if(await lastFm.nowPlaying()):
        splitTitle = await lastFm.getSplitTitle()
        await client.edit_message_text(message.chat.id, message.id, 
                                                            "▶️ **Now playing**\n🎵 "
                                                                + splitTitle[0] + "\nby:" + splitTitle[1])
    else:
        await client.edit_message_text(message.chat.id, message.id, "⏹️ Not playing anything at the moment.")

"""
    Main scrobbling cycle. Whenever scrobbling is enabled on the profile, the function checks if you're scrobbling something on last.fm
    If you are, a 5-second mute audio using as a title the title of the song will be uploaded as the current song on the profile, if not
    a placeholder is uploaded instead.
"""
async def profileScrobbler():
    try:
        while(scrobblingStatus):
            await clearAudio()
            if(await lastFm.nowPlaying()):
                await bot.add_profile_audio("file.mp3", title="▶️ Now playing", performer=(await lastFm.getCompleteName()))
            else:
                await bot.add_profile_audio("file.mp3", title="⏹️ Now playing", performer="Nothing")
            await asyncio.sleep(30)
    except KeyboardInterrupt:
        exit()

bot.run()