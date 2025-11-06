import os
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN env var not set")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)  # prefix unused now

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands synced: {len(synced)}")
    except Exception as e:
        print("Sync error:", e)

@bot.tree.command(name="me", description="Say something in roleplay style")
@app_commands.describe(message="What do you want to say?")
async def me(interaction: discord.Interaction, message: str):
    username = interaction.user.display_name
    # send a normal (non-ephemeral) message; no auto-delete
    await interaction.response.send_message(f"**{username}** {message}", ephemeral=False)

if __name__ == "__main__":
    bot.run(TOKEN)





