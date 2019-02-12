import discord
import asyncio
import youtube_dl

token10 = 'TOKEN_HERE'
client10 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client10.event
async def on_ready():
    print('Logged in!')
    await client10.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel10 = client10.get_channel(voice_id)
    vc10 = await client10.join_voice_channel(voice_channel10)
    player10 = await vc10.create_ytdl_player(url)
    player10.start()
