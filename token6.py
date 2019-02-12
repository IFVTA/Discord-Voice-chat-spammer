import discord
import asyncio
import youtube_dl

token6 = 'TOKEN_HERE'
client6 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client6.event
async def on_ready():
    print('Logged in!')
    await client6.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel6 = client6.get_channel(voice_id)
    vc6 = await client6.join_voice_channel(voice_channel6)
    player6 = await vc6.create_ytdl_player(url)
    player6.start()
