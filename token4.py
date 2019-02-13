import discord
import asyncio
import youtube_dl
import os


client4 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token4 = tokie[4].rstrip()

@client4.event
async def on_ready():
    print('Token 4: Logged in!')
    await client4.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel4 = client4.get_channel(voice_id)
    vc4 = await client4.join_voice_channel(voice_channel4)
    player4 = await vc4.create_ytdl_player(url)
    player4.start()
