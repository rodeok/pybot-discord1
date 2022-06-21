from discord import Intents
import nextcord
from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("Bot is ready!")


testingServerId = "74418098984"


@client.slash_command(name = "hello", description = "Replies with hello", guild_ids=[testingServerId])
async def hellocommand(interaction: Interaction):
    await interaction.response.send_message("Hello!")




client.run("OTc5Nzc0MzY4MzYyMzYwMzI4.XQ_Xzw.XQ_Xzw")
