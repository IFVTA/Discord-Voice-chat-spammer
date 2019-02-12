import discord
import asyncio
import youtube_dl

token5 = 'TOKEN_HERE'
client5 = discord.Client()

d = open("channelid.txt", "r")
f = open("youtubelink.txt", "r")
yturl = str(f.readline())
voice_id = str(d.readline())


@client5.event
async def on_ready():
    print('Logged in!')
    await client5.loop.create_task(main())

async def main():
    url = str(yturl)
    voice_channel5 = client5.get_channel(voice_id)
    vc5 = await client5.join_voice_channel(voice_channel5)
    player5 = await vc5.create_ytdl_player(url)
    player5.start()