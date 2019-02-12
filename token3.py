import discord
import asyncio
import youtube_dl

token3 = 'TOKEN_HERE'
client3 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client3.event
async def on_ready():
    print('Logged in!')
    await client3.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel3 = client3.get_channel(voice_id)
    vc3 = await client3.join_voice_channel(voice_channel3)
    player3 = await vc3.create_ytdl_player(url)
    player3.start()