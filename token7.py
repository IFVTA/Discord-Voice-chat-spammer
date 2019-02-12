import discord
import asyncio
import youtube_dl

token7 = 'TOKEN_HERE'
client7 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client7.event
async def on_ready():
    print('Logged in!')
    await client7.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel7 = client7.get_channel(voice_id)
    vc7 = await client7.join_voice_channel(voice_channel7)
    player7 = await vc7.create_ytdl_player(url)
    player7.start()
