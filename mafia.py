from english import get_random_words
from db import add_player
import discord
from discord.ext import commands
import threading
import time
import aioschedule as schedule
from dotenv import load_dotenv
import os
import asyncio
from multiprocessing import Process

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix= '_')

@client.command()
async def register(ctx, time, words, complexity):
    print("REGISTER")
    player = add_player(ctx.author.id, words, complexity)
    words_function = await get_words_function(player)
    
    schedule.every(int(time)).seconds.do(words_function)
    # schedule.every().day.at(time).do(words_function)


async def get_words_function(player):
    async def send_message():
        print("NAAA")
        message = player.get_new_words()
        author = await client.fetch_user(player.get_id())
        await author.send(message)
    return send_message

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
def timer():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        loop.run_until_complete(schedule.run_pending())
        time.sleep(0.1)

if __name__ == '__main__':
    schedthread = threading.Thread(target=timer)
    schedthread.start()
    client.run(TOKEN)

