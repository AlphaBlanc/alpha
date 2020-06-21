import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name="Alpha.minesv.kr", type=1))

access_token = os.environ["token"]
client.run(access_token)
