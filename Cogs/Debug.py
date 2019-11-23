import discord
from discord.ext import commands
from config import Embed_Color
from config import operators

class Debug(commands.Cog, name='Debug'):
    def __init__(self, bot):
        self.bot = bot
        print('[Cogs] Debug has been loaded Successfully!')

    @commands.command(name='fakejoin')
    async def fakejoin(self, ctx):

        try:
            if (ctx.author.id in operators) or (ctx.author.id == 324786471678771200):
                embed = discord.Embed(color=Embed_Color)

                help_desc = f"""
                Welcome {ctx.author.mention} to Kritos Network's Discord Server

                If you need assistance make sure to join our Teamspeak
                """

                embed.add_field(name='» Welcome to Kritos Network', value=help_desc)
                embed.set_footer(text='ts.kritos.net')
                await ctx.author.send(embed=embed)
                role = discord.utils.get(ctx.author.guild.roles, id=593338656203472907)
                await ctx.author.add_roles(role)
        except Exception as e:
            print(e)
