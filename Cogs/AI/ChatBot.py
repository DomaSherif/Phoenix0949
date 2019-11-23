from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import operator, discord, operator, random, ast
from gingerit.gingerit import GingerIt
from discord.ext import commands
from chatterbot import ChatBot
from config import Embed_Color
from datetime import datetime
from config import operators

chatbot = ChatBot('Phoenix', read_only=True)
parser = GingerIt()


_OP_MAP = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Invert: operator.neg,
}


class Calc(ast.NodeVisitor):

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return _OP_MAP[type(node.op)](left, right)

    def visit_Num(self, node):
        return node.n

    def visit_Expr(self, node):
        return self.visit(node.value)

    @classmethod
    def evaluate(cls, expression):
        tree = ast.parse(expression)
        calc = cls()
        return calc.visit(tree.body[0])

class AdaptorsManager:

    class MathAdaptor:

        def can_process(self, message):


            if ('*' in message) or ('/' in message) or ('-' in message) or ('+' in message):
                if 'what' in message:
                    message = message.split(" ", 1)[1]
                confidence = random.uniform(0.5, 1)
            else:
                confidence = 0

            return confidence

        def process(self, message):

            response = Calc.evaluate(message)

            return response

    class TimeAdaptor:

        def can_process(self, message):

            if ('time' in message.lower()) and ('what' in message.lower()):
                confidence = random.uniform(0.5, 1)
            else:
                confidence = 0 #random.uniform(0, 1)

            return confidence

        def process(self, message):

            now = datetime.now()

            current_time = now.strftime("%I:%M %p")

            response = 'The Current time is '+current_time

            return response

    # class ExamleAdaptor:
    #
    #     def can_process(self, message):
    #
    #         confidence = random.uniform(0, 1)
    #
    #         return confidence
    #
    #     def process(self, message):
    #
    #         response = 'Example'
    #
    #         return response

    Adaptors = [MathAdaptor() , TimeAdaptor()]

    def LogCheck(self, message):

        confidence = {}

        for Adaptor in self.Adaptors:

            confidence[Adaptor] = Adaptor.can_process(message)

        Adaptor = max(confidence, key=confidence.get)

        if confidence[Adaptor] > 0.5:
            return str(Adaptor.process(message))
        else:
            return message



#-----------------------------------------------------------------------------------------#



class ChatBot(commands.Cog, name='ChatBot'):

    def __init__(self, bot):
        self.chatbot = chatbot
        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.bot = bot
        print('[Cogs] ChatBot has been loaded Successfully!')

    @commands.command(name='chat')
    async def ChatBotInteract(self, ctx):

        async with ctx.channel.typing():

            message = ctx.message.content.split(" ", 1)[1]

            try:
                message = parser.parse(message)['result']
            except e:
                pass

            ManagerAdaptor = AdaptorsManager()

            LogCheck_repsonse = ManagerAdaptor.LogCheck(message)

            if message != LogCheck_repsonse:

                print(ctx.message.author.name, message)

                await ctx.send(f'{ctx.author.mention} ' + LogCheck_repsonse)

            else:

                print(ctx.message.author.name, message)

                await ctx.send(f'{ctx.author.mention} ' + str(chatbot.get_response(message)))




    @commands.command(name='train')
    async def TrainingCommand(self, ctx):

        try:
            option = ctx.message.content.split(" ", 1)[1]
        except:
            await ctx.message('What Kind of Training Option would like?')
            return

        if option == 'corpus-english':

            await ctx.send(':gear: **Training The AI**')

            self.trainer.train("chatterbot.corpus.english")

            await ctx.send(':heavy_check_mark: **Bot Trained**')

        elif option == 'corpus-english-greetings':

            await ctx.send(":gear: **Training The AI**")

            trainer.train("chatterbot.corpus.english.greetings")

            await ctx.send(':heavy_check_mark: **Bot Trained**')

        elif option == 'corpus-english-conversations':

            await ctx.send(":gear: **Training The AI**")

            trainer.train("chatterbot.corpus.english.conversations")

            await ctx.send(':heavy_check_mark: **Bot Trained**')

        else:

            await ctx.send(':x: Undefine Option')
