
import discord

from discord.ext import commands
from config import settings

import random


bot = commands.Bot(command_prefix = settings['prefix'])


@bot.command()
async def stupid_help(ctx):
    await ctx.send(
            'help - для хелпы, очевидно.\n',
            'check [civ, maf, com=1, don=1] - чтоб разослать роди, тупица.\n'
            )



text_tokens = ['Мирный', 'Мафия', 'Комиссар', 'Дон мафии']


@bot.command()
async def check(ctx, *args):
    roles = []
    print(args)

    for i, role in enumerate(text_tokens):
        if i < len(args):
            roles.extend([role]*int(args[i]))
        else:
            roles.append(role)

    random.shuffle(roles)
    print(roles)

    author = ctx.author
    channel = author.voice.channel
    print(author, channel.members)
    for i, member in enumerate(channel.members):
        member_role = roles[i]
        print(i, member.mention, member_role)
        await member.send(f'{author.mention} loshara, ti est {member_role}')







