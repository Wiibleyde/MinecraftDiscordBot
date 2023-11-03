import discord
from discord import app_commands
from discord.ext import commands, tasks
import os
import base64

from objects.Config import Config
from objects.Minecraft import Minecraft

bot = commands.Bot(command_prefix=Config(os.path.join(os.path.dirname(__file__), "config.yml")).get_discord_prefix(), intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is ready")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Starting..."))
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
        print(f"Commands: {synced}")
        status.start()
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    print("Bot has started and all tasks are running")

@bot.tree.command(name="server", description="Trouver les informations du serveur Minecraft")
async def server(ctx):
    server = Minecraft()
    faviconb64 = server.get_favicon()
    favicon = base64.b64decode(faviconb64.split(",")[1])
    with open("favicon.png", "wb") as file:
        file.write(favicon)
    embed = discord.Embed(
        title="Creatia", 
        description=f"Statut du serveur: {':green_circle:' if server.is_online() else ':red_circle:'}",
        color=0x28a7b0
    )
    embed.add_field(name="Motd", value=f"{server.get_motd()}")
    embed.add_field(name="Version", value=f"{server.get_version()}")
    embed.add_field(name="Joueurs", value=f"{server.get_players()}/{server.get_max_players()}")
    embed.add_field(name="Ping", value=f"{round(server.get_ping())}ms")
    embed.set_thumbnail(url="attachment://favicon.png")
    embed.set_footer(text="Creatia - Par Zelta (Bot par Wiibleyde)")
    await ctx.response.send_message(embed=embed, file=discord.File("favicon.png"), ephemeral=True)

@bot.tree.command(name="ping", description="Vérifier le ping du bot")
async def ping(ctx):
    server = Minecraft()
    faviconb64 = server.get_favicon()
    favicon = base64.b64decode(faviconb64.split(",")[1])
    with open("favicon.png", "wb") as file:
        file.write(favicon)
    embed = discord.Embed(
        title="Ping", 
        description=f"**Ping du bot :**\n{round(bot.latency * 1000)}ms",
        color=0x28a7b0
    )
    embed.add_field(name="Ping du serveur :", value=f"{round(server.get_ping())}ms")
    embed.set_thumbnail(url="attachment://favicon.png")
    embed.set_footer(text="Creatia - Par Zelta (Bot par Wiibleyde)")
    await ctx.response.send_message(embed=embed, file=discord.File("favicon.png"), ephemeral=True)

@bot.tree.command(name="ip", description="Trouver l'ip du serveur Minecraft")
async def ip(ctx):
    server = Minecraft()
    faviconb64 = server.get_favicon()
    favicon = base64.b64decode(faviconb64.split(",")[1])
    with open("favicon.png", "wb") as file:
        file.write(favicon)
    embed = discord.Embed(
        title="Creatia", 
        description=f"Statut du serveur: {':green_circle:' if server.is_online() else ':red_circle:'}",
        color=0x28a7b0
    )
    embed.add_field(name="IP", value=f"{server.config.get_minecraft_server()}:{server.config.get_minecraft_port()}")
    embed.set_thumbnail(url="attachment://favicon.png")
    embed.set_footer(text="Creatia - Par Zelta (Bot par Wiibleyde)")
    await ctx.response.send_message(embed=embed, file=discord.File("favicon.png"), ephemeral=True)

@tasks.loop(seconds=10)
async def status():
    server = Minecraft()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{server.get_players()}/{server.get_max_players()} joueurs"))

if __name__ == "__main__":
    server1 = Minecraft()
    print(f"Server is online: {server1.is_online()}")
    bot.run(Config(os.path.join(os.path.dirname(__file__), "config.yml")).get_discord_token())