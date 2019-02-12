import discord
import asyncio
import youtube_dl

token1 = 'TOKEN_HERE'
client1 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client1.event
async def on_ready():
    print('Logged in!')
    await client1.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel1 = client1.get_channel(voice_id)
    vc1 = await client1.join_voice_channel(voice_channel1)
    player1 = await vc1.create_ytdl_player(url)
    player1.start()

