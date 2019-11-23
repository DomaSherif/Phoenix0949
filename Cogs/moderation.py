import discord
from discord.ext import commands
from config import Embed_Color
from config import operators

class Moderation(commands.Cog, name='Moderation'):
    def __init__(self, bot):
        self.bot = bot
        print('[Cogs] Moderation has been loaded Successfully!')

    #This is for permnant mute
    @commands.command(name='mute')
    async def mute(self, ctx):
        if (ctx.author.id in operators) or ctx.author.id == 324786471678771200:
            author = ctx.message.author
            if "muted" in [y.name.lower() for y in author.roles]:
                target = ctx.message.mentions[0]
                role = discord.utils.get(ctx.guild.roles, name="muted")
                await target.remove_roles(role)
                await ctx.message.delete()
                response = await ctx.channel.send(":speaking_head: **{} was unmuted!**".format(target.mention))
                await asyncio.sleep(5)
                await response.delete()
            else:
                target = ctx.message.mentions[0]
                role = discord.utils.get(ctx.guild.roles, name="muted")
                await target.add_roles(role)
                await ctx.message.delete()
                response = await ctx.channel.send(":speak_no_evil: **{} was muted!**".format(target.mention))
                await asyncio.sleep(5)
                await response.delete()
        else:
            await ctx.channel.send(':lock: **Sorry, But you need permission use this command!**')

    @commands.command(name='kick')
    async def kick(self, ctx):
        if ctx.message.mentions:
            user = ctx.message.mentions[0]
            if (ctx.author.id in operators) or ctx.author.id == 324786471678771200:
                await user.kick()
                inform = await ctx.send('**User has been kicked from the server**')
                await asnycio.sleep(5)
                await inform.delete()
            else:
                await ctx.send(':lock: **Sorry, But you need permission use this command!**')
        else:
            await ctx.send(':x: **Please mention the user!**')

    @commands.command(name='ban')
    async def ban(self, ctx):
        if ctx.message.mentions:
            user = ctx.mentions[0]
            if (ctx.author.id in operators) or ctx.author.id == 324786471678771200:
                await user.ban(reason='The ban hammer has spoken')
                inform = await ctx.send('**User has been kicked from the server**')
                await asnycio.sleep(5)
                await inform.delete()
            else:
                await ctx.send(':lock: **Sorry, But you need permission use this command!**')
        else:
            await ctx.send(':x: **Please mention the user!**')
