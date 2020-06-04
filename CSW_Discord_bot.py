import discord
import time

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
    check = 1
    week = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
    if message.content.startswith("!hello"):
        f = open('discord data/hello.txt','r')
        h = f.readlines()
        now = time.localtime()
        n = time.localtime().tm_wday
        await message.channel.send(gotest(h)+"\n"
                                   +"```"
                                   +"```"+"cs"+"\n"
                                   +"'Today is "+("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))+ " " +week[n] + "'"+"\n"
                                   +"'This time is "+("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
                                   +"'```")
    if message.content.startswith("!help"):
        f = open('discord data/help.txt','r')
        h = f.readlines()
        await message.channel.send(gotest(h))
    if message.content.startswith("!time"):
        now = time.localtime()
        await message.channel.send("```cs"+"\n"+"'"+("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))+"'```")
    if message.content.startswith("!day"):
        now = time.localtime()
        n = time.localtime().tm_wday
        await message.channel.send("```cs"+"\n"+"'"+(("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))+ " " +week[n])+"'```")
    if message.content.startswith("!now"):
         now = time.localtime()
         n = time.localtime().tm_wday
         await message.channel.send("```cs"+"\n"+"'"+(("%04d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday))+ " " +week[n])+"'"+"\n"
                                    +"'"+("%02d:%02d:%02d" % (now.tm_hour, now.tm_min, now.tm_sec))
                                    +"'```")
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
f.close()
