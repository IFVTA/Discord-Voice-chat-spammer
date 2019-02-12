import discord
import asyncio
import youtube_dl

token2 = 'TOKEN_HERE'
client2 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client2.event
async def on_ready():
    print('Logged in!')
    await client2.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel2 = client2.get_channel(voice_id)
    vc2 = await client2.join_voice_channel(voice_channel2)
    player2 = await vc2.create_ytdl_player(url)
    player2.start()