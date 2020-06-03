import discord

def gotest(list1):
    j = ""
    for i in range(len(list1)):
        j = j + list1[i]
    return j
client = discord.Client()
token="your_token"

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Hello World")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!hello"):
        j = ""
        f = open('discord data/hello.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
    if message.content.startswith("!help"):
        f = open('discord data/help.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
    if message.content.startswith("!python"):
        f = open('discord data/python.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
    if message.content.startswith("!java"):
        f = open('discord data/java.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
    if message.content.startswith("!html"):
        f = open('discord data/html.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
    if message.content.startswith("!c++"):
        f = open('discord data/c++.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
    elif message.content.startswith("!c#"):
        f = open('discord data/c#.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
    elif message.content.startswith("!c"):
        f = open('discord data/c.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
    if message.content.startswith("!go"):
        f = open('discord data/go.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
        
client.run(token)
f.close
