import webbrowser
import discord
import asyncio
import os, random
from googlesearch import search 
from bot_db_utils import save_search_data, fetch_data 

bot = discord.Client()

#async as they are running concurrently
#await if there is something else to be done while waiting for value, it should go ahead and run

token = "Nzg4NDczMzM5MjkwMDU4ODAy.X9kBBQ.Loel5xpImkv1tXQ0Edi7I28H2C4"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_member_join(member):
    if member.id == bot.id:
        return
    channel = discord.utils.get(bot.guilds[0].channels, name = "general")
    response = f"welcome, {member.name}."
    await channel.send(response)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    keywords =  [ "hi", "hello", "hey"]
    channel = message.channel
    msg = message.content.lower()
    
    if message.content.lower() in keywords:
        response = f" \n Hey!!"
        await channel.send(response)

    if msg.startswith("!google"):
         for response in search_google(msg, message):   
             await channel.send(response)

    if msg.startswith("!recent"):
        await channel.send("some recent responses are :")
        for response in get_recent_data(msg, message):
            await channel.send(response) 


def search_google(msg, message):
    if len(msg.split(None,1)) < 2:
        response = "please enter something to search on google"
        yield response
    else:
        query_keyword = msg.split(None,1)[1]
        for j in search(query_keyword, tld="co.in", num=5, stop=5, pause=2):
            response = j + "\n" 
            print (j)
            yield response

    save_search_data(message.author, query_keyword, j)


def get_recent_data(msg, message):
    query_keyword = msg.split(None, 1)[1]
    results = fetch_data(message.author, query_keyword)
    if len(results) ==0:
        response = f"No recent search for {query_keyword}"
        yield response 
    else:
        for j in results: #('neharika#0053', 'iphone11', datetime.datetime(2020, 12, 17, 23, 46, 26), link) db rows
            print (j)     #we can here return recent links as well.
            response =  j[1]
            yield response        


bot.run(token)

