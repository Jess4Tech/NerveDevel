import discord
import logging
from discord.ext import commands
description = '''Nerve bot is a W.I.P bot meant to help with basic tasks.'''
bot = commands.Bot(command_prefix='!', description=description)
maker = 'Nerve bot is the property of Jess Gaming. Its production and release rights belong to Jess Gaming'
prefix = '!'
commands = 'Info | Ready | Kys | (COMING SOON)'

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = discord.Client()

def message_returned():
	message = input('Enter a phrase: ')
	return message
@bot.event
async def on_ready():
	print('------')
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')

@bot.command(description = 'Shows information on Nerve Bot.')
async def info():
	'''Shows information on Nerve Bot.'''
	await bot.say('CREATOR: ' + maker)
	await bot.say('DESCRIPTION: ' + description)
	await bot.say('PREFIX: ' + prefix)
	await bot.say('COMMANDS: ' + commands)

@bot.command(description = 'Sets up Nerve Bot for running.')
async def ready():
	'''Sets up Nerve Bot for running.'''
	await bot.change_presence(game=discord.Game(name='with some neurons...'))
	await bot.say('Ready to go!')
@bot.command(pass_context=True, aliases=["say"])
async def say_command(ctx, channel:discord.Channel, *, thing_to_say): 
	await bot.send_message(channel, thing_to_say)
@bot.command(description = 'Tests your ping')
async def ping(ctx):
	'''Tests your ping'''    
	return await ctx.send_message('Pong! {0}'.format(round(bot.latency, 1)))
@bot.command(description = 'Kills Nerve Bot')
async def kys():
    '''Poor Nerve Bot'''
    await bot.logout()