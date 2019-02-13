import discord
import asyncio
import youtube_dl
import os


client8 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token8 = tokie[8].rstrip()
			
@client8.event
async def on_ready():
    print('Token 8: Logged in!')
    await client8.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel8 = client8.get_channel(voice_id)
    vc8 = await client8.join_voice_channel(voice_channel8)
    player8 = await vc8.create_ytdl_player(url)
    player8.start()
