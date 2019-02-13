import discord
import asyncio
import youtube_dl
import os


client7 = discord.Client()

t = open("tokens.txt", "r")
c = open("channelid.txt", "r")
y = open("youtubelink.txt", "r")
tokie = t.readlines()
yturl = str(y.readline())
voice_id = str(c.readline())
token7 = tokie[7].rstrip()
			
@client7.event
async def on_ready():
    print('Token 7: Logged in!')
    await client7.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel7 = client7.get_channel(voice_id)
    vc7 = await client7.join_voice_channel(voice_channel7)
    player7 = await vc7.create_ytdl_player(url)
    player7.start()
