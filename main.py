import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


said_hello = set()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # print(message)
    if message.author == client.user or message.author in said_hello:
        return
    await message.channel.send(f'Hello {message.author}')
    said_hello.add(message.author)

client.run(
    'MTEyNzY5NTI5NjgxODgzOTU5Mw.GK8Hnk.wRWUpaYB-JNCVuwoIFiQbL5i6zZiAaauD0k_t8')

#     The first line imports the discord.py library.
#     The second line imports the os library, but this is only used for getting the TOKEN variable from the .env file. If you are not using a .env file, you do not need this line.
#     Next, we create an instance of a Client. This is the connection to Discord.
#     The @client.event() decorator is used to register an event. This is an asynchronous library, so things are done with callbacks. A callback is a function that is called when something else happens. In this code, the on_ready() event is called when the bot is ready to start being used. Then, when the bot receives a message, the on_message() event is called.
#     The on_message() event triggers each time a message is received but we don't want it to do anything if the message is from ourselves. So if the Message.author is the same as the Client.user the code just returns.
#     Next, we check if the Message.content starts with '$hello'. If so, then the bot replies with 'Hello!' to the channel it was used in.
#     Now that the bot is set up, the final line runs the bot with the login token. It gets the token from out .env file.
