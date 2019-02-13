import discord
import asyncio
import youtube_dl
import os


client6 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token6 = tokie[6].rstrip()
			
@client6.event
async def on_ready():
    print('Token 6: Logged in!')
    await client6.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel6 = client6.get_channel(voice_id)
    vc6 = await client6.join_voice_channel(voice_channel6)
    player6 = await vc6.create_ytdl_player(url)
    player6.start()
