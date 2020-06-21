import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(clientclient.user.name)
    print(client.user.id)
    print("==========")
    game = discord.Game("서버주소: Alpha.minesv.kr")
    await app.change_presence(status=discord.Status.online, activity=game)



clinet.run(os.environ['token'])
