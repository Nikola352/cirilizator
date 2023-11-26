import discord
from configparser import ConfigParser

config = ConfigParser()
config.read('config.conf')
TOKEN = config.get('Discord', 'api_key', raw=True)
GUILD = config.get('Discord', 'guild_id', raw=True)
CHANNEL_ID = config.get('Discord', 'channel_id', raw=True)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = discord.Client(intents=intents)

messages = []


@bot.event
async def on_ready():
    print("Discord bot is in " + str(len(bot.guilds)) + " guilds.")


@bot.event
async def on_message(message):
    if message.channel.id == int(CHANNEL_ID):
        messages.append({
            "author": str(message.author),
            "content": message.content
        })


def run_discord_bot():
    bot.run(TOKEN)
