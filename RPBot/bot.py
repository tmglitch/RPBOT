import os
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN env var not set")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands synced: {len(synced)}")
    except Exception as e:
        print("Sync error:", e)

# Slash command /me
@bot.tree.command(name="me", description="Say something in roleplay style")
@app_commands.describe(message="The message you want to say")
async def me(interaction: discord.Interaction, message: str):
    username = interaction.user.display_name
    await interaction.response.send_message(f"**{username}** {message}")

bot.run(TOKEN)

