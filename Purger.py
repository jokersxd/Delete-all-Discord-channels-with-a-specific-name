from colorama import Fore, init, Style
from discord.ext import commands
import discord
import ctypes
import os

token = ''

client = commands.Bot(command_prefix='-', self_bot=True)
client.remove_command('help')

@client.event
async def on_connect():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW('Discord Channel Purger | Developed by jokers')
    init(convert=True, autoreset=True)
    print(Fore.GREEN + '\n -- ' + Fore.WHITE + Style.BRIGHT + 'Ready')
    print(' ')

@client.command()
async def delete(ctx, *, name=None):
    if name == None:
        print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'Cannot delete channel/s without name to delete from')
    else:
        for channel in ctx.guild.channels:
            if str(name) in channel.name:
                print(Fore.GREEN + '[DELETED] ' + Fore.WHITE + Style.BRIGHT + str(channel.name))
                await channel.delete()

client.run(token, bot=False)
