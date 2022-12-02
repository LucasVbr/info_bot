import discord
import config
import asyncio
import requests
import shlex

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# bot=commands.Bot(command_prefix ="$")

url = "http://localhost:3000"


@client.event
async def on_ready():
    print("✔ Connecté")


@client.event
async def on_message(message):
    msg = message.content
    if message.author.bot:
      return

    if msg.startswith("!help"):
        await message.channel.send("!message - envoie un message a la page\n"
        + "!background - change la couleur du fond d'écran de la page"
        + "!messagesColor - change la couleur du texte de la page")

    if msg.startswith("!message "):
        text = msg.split(" ", 1)[1]
        requests.get(f"{url}/message?text={text}")

    if msg.startswith("!background "):
        background = msg.split(" ", 1)[1]
        requests.get(f"{url}/background?background={background}")

    if msg.startswith("!messagesColor "):
        color = msg.split(" ", 1)[1]
        requests.get(f"{url}/color?color={color}")

async def setup():
    pass


async def main():
    await setup()
    await client.start(config.TOKEN)


asyncio.run(main())
