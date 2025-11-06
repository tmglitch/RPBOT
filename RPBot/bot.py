import os
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN environment variable not set")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print("Slash sync error:", e)

# /me command – posts "**Username** *message*" publicly and deletes interaction
@bot.tree.command(name="me", description="Speak in a roleplay style (everyone sees it)")
@app_commands.describe(message="The message you want to say")
async def me(interaction: discord.Interaction, message: str):
    username = interaction.user.display_name

    # Send the visible message
    await interaction.response.send_message(f"**{username}** *{message}*")

    # Delete the original interaction (the gray "User used /me" bar)
    try:
        await interaction.delete_original_response()
    except Exception as e:
        print("Couldn't delete original interaction:", e)

bot.run(TOKEN)



