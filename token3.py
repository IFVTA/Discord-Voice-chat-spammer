import discord
import asyncio
import youtube_dl
import os


client3 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token3 = tokie[3].rstrip()

@client3.event
async def on_ready():
    print('Token 3: Logged in!')
    await client3.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel3 = client3.get_channel(voice_id)
    vc3 = await client3.join_voice_channel(voice_channel3)
    player3 = await vc3.create_ytdl_player(url)
    player3.start()
