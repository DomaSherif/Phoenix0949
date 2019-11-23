from discord.ext import commands
from config import Embed_Color
from config import operators
from config import Logging_Channel_ID
import discord

class Logger(commands.Cog, name='Logger'):
    def __init__(self, bot):
        self.bot = bot
        if not Logging_Channel_ID:
            print('[Alert] Logger Cog Cannot be ran because Logging_Channel_ID is undefine')
            return
        print('[Cogs] Logger has been loaded Successfully!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if Logging_Channel_ID:
            Channel_ID = Logging_Channel_ID
            embed=discord.Embed(color=Embed_Color, description=member.mention + " " + member.name+"#"+member.discriminator)
            embed.set_author(name=" Member Joined",icon_url=member.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            await channel.send(embed=embed)
        else:
            print('[Alert] Logger Cog Cannot be ran because Logging_Channel_ID is undefine')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if Logging_Channel_ID:
            Channel_ID = Logging_Channel_ID
            embed=discord.Embed(color=Embed_Color, description=member.mention + " " + member.name+"#"+member.discriminator)
            embed.set_author(name="Member Left",icon_url=member.avatar_url)
            embed.set_thumbnail(url=member.avatar_url)
            await channel.send(embed=embed)
