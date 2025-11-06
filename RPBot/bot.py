import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN env var not set")

intents = discord.Intents.default()
intents.message_content = True  # Needed to read messages

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="me", help="Roleplay-style message that replaces your message. Usage: /me your text")
@commands.guild_only()
async def me_command(ctx: commands.Context, *, message: str = None):
    if not message:
        return await ctx.reply("Usage: `/me your text`", mention_author=False)

    try:
        await ctx.message.delete()
    except discord.Forbidden:
        return await ctx.send("I need **Manage Messages** permission to delete your command.")
    except discord.HTTPException:
        pass

    username = ctx.author.display_name
    await ctx.channel.send(f"**{username}** {message}")

bot.run(TOKEN)
