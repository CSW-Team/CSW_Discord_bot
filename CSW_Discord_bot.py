import discord

client = discord.Client()

token="NzE2MTY5NTYyMjYxMDI4OTA1.XtYM3g.loM5FOZzpK1uxRHXNgnrj0T2b1g"

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("Hello World")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!hello"):
        await message.channel.send('```diff\n-Hello\n-I am Hello World Bot\n-I will tell you how to make hello world program\n-If you do not how to use me, send me -help```')
    if message.content.startswith("!help"):
        await message.channel.send("```diff\n-Write '!' + programming language that you want\n-I can tell you everything on this list\n-python\n-java\n-c/c++\n-c#\n-html\n-go```")
    if message.content.startswith("!python"):
        await message.channel.send('```python\nprint("Hello World")```')
    if message.content.startswith("!java"):
        await message.channel.send('```java\npublic class HelloWorld {\n    public static void main(String args[]) {\n        System.out.println("Hello World");\n    }\n}```')
    if message.content.startswith("!html"):
        await message.channel.send('```html\n<html>\n  <body>\n    hello world!\n  </body>\n</html>```')
    if message.content.startswith("!c++"):
        await message.channel.send('```c++\n#include <iostream>\n\nusing namespace std;\n\ni8nt main()\n{\n	cout << "Hello World" << endl;\n	return 0;\n}```')
    elif message.content.startswith("!c#"):
        await message.channel.send('```c\nusing System;\nusing System.Collections.Generic;\nusing System.Linq;\nusing System.Text;\nusing System.Threading.Tasks;\n\nnamespace ConsoleApp1\n{\n    class Program\n    {\n        static void Main(string[] args)\n        {\n            Console.WriteLine("Hello World");\n        }\n    }\n}```')
    elif message.content.startswith("!c"):
        await message.channel.send('```c\n#include <stdio.h>\n\nint main()\n{\n    printf("Hello, world!");\n\n    return 0;\n}```')
    if message.content.startswith("!go"):
        await message.channel.send('```go\npackage main\n\nimport "fmt"\n\nfunc main()\n{\n	fmt.Println("Hello, World")\n}```')
        
client.run(token)
