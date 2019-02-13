import discord
import asyncio
import youtube_dl
import os


client1 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token1 = tokie[1].rstrip()

@client1.event
async def on_ready():
    print('Token 1: Logged in!')
    await client1.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel1 = client1.get_channel(voice_id)
    vc1 = await client1.join_voice_channel(voice_channel1)
    player1 = await vc1.create_ytdl_player(url)
    player1.start()

