# bot.py
import os

import discord
from discord.utils import to_json
from dotenv import load_dotenv
from prettytable import PrettyTable
from english import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    
def is_command (msg): # Checking if the message is a command call
    if len(msg.content) == 0:
        return False
    elif msg.content.split()[0] == '_scan' or msg.content.split()[0] == '_learn':
        return True
    else:
        return False
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('_'):

        cmd = message.content.split()[0].replace("_","")
        if cmd == 'scan':
            
            limit_messages = 10000
            limit_words = 10
            frequency = 0.5
            
            data = await get_messages_data(message, limit_messages)
            
            result = f'Ant finished scanning {limit_messages} messages: \n'
            
            for user in data:
                result += f'{user}: \n'
                
                sort_orders = sorted(data[user].items(), key=lambda x: x[1], reverse=True)
                
                words = []
                
                for word, number in sort_orders:
                    if len(words) == limit_words:
                        break
                    if get_frequency(word) < frequency:
                        words.append((word, number))
                
                t = PrettyTable(['Word', 'Count'])
                t.align = "l"
                t.align["Count"] = "r"
                for word, number in words:
                    t.add_row([word, number])
                    
                result += t.get_string()
                result += "\n\n"
            
            
            await message.channel.send(result)
        
        if cmd == 'learn':
            
            limit_messages = 1000
            limit_words = 10
            frequency = 0.3
            
            data = await get_messages_data(message, limit_messages)
            
            for user in data:
                result = f'Recommendation for {user}: \n'
                
                recomendations = []
                
                sort_orders = sorted(data[user].items(), key=lambda x: x[1], reverse=True)
                
                words = []
                
                for word, number in sort_orders:
                    if len(words) == limit_words:
                        break
                    if get_frequency(word) < frequency:
                        words.append((word, number))
                
                t = PrettyTable(['Word', 'Example'])
                t.align = "l"
                t.align["Count"] = "r"
                for word, number in words:
                    synonims = get_synonims(word)
                    
                    for synonim in synonims:
                        if synonim not in data[user].keys() and synonim not in recomendations and len(recomendations) < limit_words:
                            recomendations.append(synonim)
                            
                            example = get_example(synonim)
                            
                            t.add_row([synonim, example[0]['definition']])
                    
                result += t.get_string()
                result += "\n\n"
            
                await message.channel.send(result)
        if cmd == 'register':
            print("register")
            

async def get_messages_data(message, limit):
    data = {}
    async for msg in message.channel.history(limit=limit): # As an example, I've set the limit to 10000
                
        if msg.author != client.user and not msg.author.bot:                        # meaning it'll read 10000 messages instead of           
            if not is_command(msg):                          # the default amount of 100     
                
                if msg.author.name not in data:
                    data[msg.author.name] = {}
                    
                for word in msg.content.split():
                    if word not in data[msg.author.name]:
                        data[msg.author.name][word] = 0
                    data[msg.author.name][word] += 1
    
    return data

client.run(TOKEN)