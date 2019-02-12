import discord
import asyncio
import youtube_dl

token4 = 'TOKEN_HERE'
client4 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client4.event
async def on_ready():
    print('Logged in!')
    await client4.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel4 = client4.get_channel(voice_id)
    vc4 = await client4.join_voice_channel(voice_channel4)
    player4 = await vc4.create_ytdl_player(url)
    player4.start()