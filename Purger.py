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
    await ctx.message.delete()
    if name == None:
        print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'Cannot delete channel/s without name to delete from')
    else:
        try:
            for channel in ctx.guild.channels:
                if str(name) in channel.name:
                    try:
                        await channel.delete()
                        print(Fore.GREEN + '[DELETED] ' + Fore.WHITE + Style.BRIGHT + str(channel.name))
                    except discord.errors.Forbidden:
                        print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + 'No permissions to delete channel/s')
                        break
        except Exception as e:
            print(Fore.RED + '[ERROR] ' + Fore.WHITE + Style.BRIGHT + str(e))

client.run(token, bot=False)
