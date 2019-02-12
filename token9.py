import discord
import asyncio
import youtube_dl

token9 = 'TOKEN_HERE'
client9 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client9.event
async def on_ready():
    print('Logged in!')
    await client9.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel9 = client9.get_channel(voice_id)
    vc9 = await client9.join_voice_channel(voice_channel9)
    player9 = await vc9.create_ytdl_player(url)
    player9.start()