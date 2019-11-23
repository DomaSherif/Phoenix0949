#rom Cogs.AI.ChatBot import MyTimeAdaptor
from Cogs.moderation import Moderation
from Cogs.AI.ChatBot import ChatBot
from Cogs.greeting import Greetings
import discord, asyncio, aiohttp
from discord.ext import commands
from Cogs.Logger import Logger
from datetime import datetime
from Cogs.Debug import Debug
from config import *


client = commands.Bot(command_prefix=BOT_PREFIX)
client.remove_command('help')


async def calculate_age(born):
    today = datetime.today()
    if today.year - born.year - ((today.month, today.day) < (born.month, born.day)) <= 0:
        age = today.month - born.month
        if age <= 0:
            age = today.day - born.day
            if age != 1:
                age = str(today.day - born.day)+" Days"
            else:
                age = str(today.day - born.day)+" Days"
        else:
            age = str(age)+" Month(s)"
    else:
        age = str(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))+ " Year(s)"
    return age

async def permission_calculator(member):

    print(dir(member))
    value = member.guild_permissions.value


    current_permisisons = ''
    for perm in permissions:
        if value & perm[1] == perm[1]:
            current_permisisons += perm[0]+', '
    return current_permisisons

async def get_online_users(guild):
    online = 0
    for member in guild.members:
        if str(member.status) != 'offline':
            online += 1
    return online

async def get_humans(guild):
    humans = 0
    for member in guild.members:
        if not member.bot:
            humans += 1
    return humans

async def get_bots(guild):
    bots = 0
    for member in guild.members:
        if member.bot:
            bots += 1
    return bots

@client.event
async def on_ready():

    if Cogs['Greetings']:
        client.add_cog(Greetings(client))
    if Cogs['Debug']:
        client.add_cog(Debug(client))
    if Cogs['Moderation']:
        client.add_cog(Moderation(client))
    if Cogs['Logger']:
        client.add_cog(Logger(client))
    if Cogs['ChatBot']:
        client.add_cog(ChatBot(client))

    print(client.user.name + ' is ready!')
    activity = discord.Activity(name='Debuging The Code', type=discord.ActivityType.playing)
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):

    if message.author.bot:
        return

    print()
    if message.guild is None:
        print('@DM')
    else:
        print('@'+message.guild.name)
    try:
        print('#' + message.channel.name)
    except UnicodeEncodeError:
        print('#Undefine')
    print(message.author.name + ' => ' + message.content)
    print()


    if "muted" in [y.name.lower() for y in message.author.roles]:
        await message.delete()
        return

    for word in message.content.split():
        if word in badwords:
            await message.delete()
            warning = await message.channel.send('{0.author.mention} **Please moderate your langauge**'.format(message))
            await asyncio.sleep(3)
            await warning.delete()
            return

    if ('https://' in message.content) or ('http://' in message.content):
        if not Advertising_URLs:
            await message.delete()
            warn = await message.channel.send(message.author.mention + " **Sending URLs is not allowed.**")


    await client.process_commands(message)

@client.command(name='purge', pass_context = True)
async def purge(ctx, number):
    if ctx.author.id in operators:
        async for message in ctx.message.channel.history(limit=int(number)):
            await message.delete()
        alert = await ctx.send('**'+str(number)+' Total Message delete!**')
        await asyncio.sleep(3)
        await alert.delete()
    else:
        await ctx.channel.send(':lock: **Sorry, But you need permission use this command!**')

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(color=0x71be29)

    help_desc = f"""
    `!help` Shows this command
    `!mute` Mutes a user.
    `!ban` Bans a user.
    `!kick` Kicks a user.
    `!purge` Removes amount of messages.
    `!userinfo` Shows information about the mentioned user.
    `!serverinfo` Shows information about the current server.
    """

    embed.add_field(name='Help menu', value=help_desc)
    embed.set_thumbnail(url=client.user.avatar_url)
    try:
        the_creator = client.get_user(324786471678771200)
        embed.set_footer(text='This bot was made by ' + the_creator.name+"#"+the_creator.discriminator)
    except:
        pass
    await ctx.message.channel.send(embed=embed)

@client.command(name='userinfo', pass_context=True)
async def userinfo(ctx):
    if ctx.message.mentions:
        target = ctx.message.mentions[0]
    else:
        target = ctx.author
    embed=discord.Embed(title="@"+target.name, color=Embed_Color)
    embed.set_author(name=target.name + "#" + target.discriminator, icon_url=target.avatar_url)
    embed.set_thumbnail(url=target.avatar_url)
    embed.add_field(name="Status", value=str(target.status), inline=True)
    embed.add_field(name="Joined", value=target.joined_at.ctime(), inline=True)
    current_roles = ''
    for role in target.roles:
        if not role == ctx.guild.default_role:
            current_roles += role.mention+" "

    embed.add_field(name="Roles [" + str(len(current_roles.split())) + "]", value=current_roles, inline=True)
    embed.add_field(name="Key Permissions", value=await permission_calculator(target), inline=True)
    if target.id == ctx.guild.owner.id:
        embed.add_field(name="Acknowledgements", value='Server Owner', inline=True)
    elif target.guild_permissions.value & 8 == 8:
        embed.add_field(name="Acknowledgements", value='Server Admin', inline=True)
    embed.add_field(name="Account Age", value=await calculate_age(target.created_at), inline=True)
    embed.set_footer(text="ID: "+str(target.id) + " • Requested by "+ctx.author.name+"#"+ctx.author.discriminator)
    embed.add_field(name="Join Position", value="None", inline=True)
    embed.add_field(name="Registered", value=target.created_at.ctime(), inline=True)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def serverinfo(ctx):
    embed=discord.Embed(color=Embed_Color)
    embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
    embed.add_field(name='Owner', value=ctx.guild.owner.name+"#"+ctx.guild.owner.discriminator, inline=True)
    embed.add_field(name='Region', value=ctx.guild.region, inline=True)
    embed.add_field(name='Channel Categories', value=len(ctx.guild.categories), inline=True)
    embed.add_field(name='Text Channels', value=len(ctx.guild.text_channels), inline=True)
    embed.add_field(name='Voice Channels', value=len(ctx.guild.voice_channels), inline=True)
    embed.add_field(name='Members', value=len(ctx.guild.members), inline=True)
    embed.add_field(name='Humans', value=await get_humans(ctx.guild), inline=True)
    embed.add_field(name='Bots', value=await get_bots(ctx.guild), inline=True)
    embed.add_field(name='Online', value=await get_online_users(ctx.guild), inline=True)
    embed.add_field(name='Roles', value=len(ctx.guild.roles), inline=True)
    embed.add_field(name='Age', value=await calculate_age(ctx.guild.created_at), inline=True)
    embed.add_field(name='Highest Role', value=ctx.guild.owner.top_role.mention, inline=True)
    embed.set_footer(text="ID: "+str(ctx.guild.id) + " • Requested by "+ctx.author.name+"#"+ctx.author.discriminator)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def reload(ctx):
    if (ctx.author.id == 324786471678771200) or (ctx.author.id in operators):
        await ctx.send(':floppy_disk: **Reloading...**')
        await client.logout()
        exit()
    else:
        await ctx.send(':lock: **Sorry but this command is for developer use only**')

client.run(TOKEN, bot=True, reconnect=True)
