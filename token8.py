import discord
import asyncio
import youtube_dl

token8 = 'TOKEN_HERE'
client8 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client8.event
async def on_ready():
    print('Logged in!')
    await client8.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel8 = client8.get_channel(voice_id)
    vc8 = await client8.join_voice_channel(voice_channel8)
    player8 = await vc8.create_ytdl_player(url)
    player8.start()