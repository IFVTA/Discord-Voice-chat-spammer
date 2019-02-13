import discord
import asyncio
import youtube_dl
import os


client10 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token10 = tokie[10].rstrip()

@client10.event
async def on_ready():
    print('Token 10: Logged in!')
    await client10.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel10 = client10.get_channel(voice_id)
    vc10 = await client10.join_voice_channel(voice_channel10)
    player10 = await vc10.create_ytdl_player(url)
    player10.start()
