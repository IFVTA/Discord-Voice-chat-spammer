import discord
import asyncio
import youtube_dl
import os


client2 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token2 = tokie[2].rstrip()

@client2.event
async def on_ready():
    print('Token 2: Logged in!')
    await client2.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel2 = client2.get_channel(voice_id)
    vc2 = await client2.join_voice_channel(voice_channel2)
    player2 = await vc2.create_ytdl_player(url)
    player2.start()
