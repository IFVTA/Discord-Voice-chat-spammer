import discord
import asyncio
import youtube_dl
import os


client5 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token5 = tokie[5].rstrip()
			
@client5.event
async def on_ready():
    print('Token 5: Logged in!')
    await client5.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel5 = client5.get_channel(voice_id)
    vc5 = await client5.join_voice_channel(voice_channel5)
    player5 = await vc5.create_ytdl_player(url)
    player5.start()
