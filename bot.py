# bot.py
import os

import random
from discord import Member

from discord.ext import commands
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'MTAxNDcyMDc3ODg2MTgxMzgyMg.GDJes4._h9PGBi85C1s3lRvLmZbNkry50h-oejhxZU7DY'
GUILD = 'RONIN'
intents = discord.Intents.default()
intents.members = True
# client = discord.Client(intents=intents)

# @client.event
# async def on_ready():
#     for guild in client.guilds:
#         if guild.name == GUILD:
#             break

#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )
#     members = '\n - '.join([member.name for member in guild.members])
#     print(f'Guild Members:\n - {members}')

# client.run(TOKEN)


bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.command(name='99', help='- random quote.')
@commands.has_role('master')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='ping', help='- pinging the bot.')
@commands.has_role('master')
async def ping(ctx):
    await ctx.send("pong!")

@bot.command(name='boss', help='- show boss\'s status.')
@commands.has_role('master')
async def boss(ctx):
    user = bot.get_user(361499404844138498)
    print(user)
    boss = str(user)
    print(user.discord.Status)
    await ctx.send('test')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.event
async def on_member_update(before, after):
    if before.status is discord.Status.idle and after.status is discord.Status.online:
        print('was offline then online')
        channel = bot.get_channel(1014743700850618388)  # notification channel
        print("online")
        await channel.send(f'{after.name} is now {after.status}')



# @bot.event
# async def on_member_update(prev,cur):       


#     # games = ["valorant", "overwatch", "rocket league", "minecraft", "stardew valley"]
    
#     # print(cur.activity.name.lower())
#     # if cur.activity and cur.activity.name.lower() in games:
#     #         #do something
#     game = [i for i in after.activities if str(i.type) == "playing"]
#     if game:
#         print(game[0].name)
#         await cur.send(game[0].name)

bot.run(TOKEN)