import discord
from configparser import ConfigParser

config = ConfigParser()
config.read('config.conf')
TOKEN = config.get('Discord', 'api_key', raw=True)
GUILD = config.get('Discord', 'guild_id', raw=True)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = discord.Client(intents=intents)

messages = []


@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")


@bot.event
async def on_message(message):
    messages.append({
        "author": str(message.author),
        "content": message.content
    })


def run_discord_bot():
    bot.run(TOKEN)
