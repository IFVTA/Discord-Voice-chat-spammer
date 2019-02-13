import discord
import asyncio
import youtube_dl
import os


client9 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token9 = tokie[9].rstrip()
			
@client9.event
async def on_ready():
    print('Token 9: Logged in!')
    await client9.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel9 = client9.get_channel(voice_id)
    vc9 = await client9.join_voice_channel(voice_channel9)
    player9 = await vc9.create_ytdl_player(url)
    player9.start()
