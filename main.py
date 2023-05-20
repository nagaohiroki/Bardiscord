import os
import discord
import Bard


intents = discord.Intents.all()
client = discord.Client(intents=intents)
bard_bot : Bard.Chatbot = Bard.Chatbot(os.environ['BARD_TOKEN'])


@client.event
async def on_ready():
    print('Bard bot login')


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.name != 'ai':
        if client.user not in message.mentions:
            return
    content = f'{message.author.name}:{message.content}'
    ask = bard_bot.ask(content)
    await message.channel.send(ask['content'])


client.run(os.environ['BARD_DISCORD_TOKEN'])
