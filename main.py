import discord
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import re

#Variables and Configurations
Owner_ID = '324786471678771200' #here is the owner of the server ID
Admin_ID = '338857791177490434' #here is the admin of the server ID
MyChannel = "461140442688258048" #here is the Channel ID that only the bot can chat in it!

client = discord.Client()
bot = ChatBot('Pheonix')
#bot.set_trainer(ListTrainer)

@client.event
async def on_message (message):

	#Checks if the the msg is from him self or not
	if message.author == client.user:
		return

	#Check if someone said 'Hey Pheonix'! then he will respond to this msg!
	elif message.content.startswith('hey Pheonix'):
		print(message.content)
		msg = 'Hi! {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

	#check if someone Typed the command !say
	elif message.content.startswith('!say'):
		#check if who's typed this Command is the Owner or not
		if message.author.id == Owner_ID:
			print(message.content)
			reg_ex = re.search('!say (.+)', message.content)
			if reg_ex:
				saying = reg_ex.group(1)
				print(saying)
				await client.send_message(message.channel, saying)

		else:
			if message.author.roles == Admin_ID:
				print(message.content)
				reg_ex = re.search('!say (.+)', message.content)
				if reg_ex:
					saying = reg_ex.group(1)
					print(saying)
					await client.send_message(message.channel, saying)
			else:
				msg = 'Sorry, but you are not allowed to use this command!'
				await client.send_message(message.channel, msg)

	elif message.content.startswith('!status'):
		if message.author.id == Owner_ID:
			print(message.content)
			reg_ex = re.search('!status (.+)', message.content)
			if reg_ex:
				status = reg_ex.group(1)
				print(status)
				if status == 'online':
					msg = 'chaning my Status to Online!'
					await client.send_message(message.channel, msg)
					await client.change_presence(status=discord.Status("Online"))

				elif status == 'idle':
					msg = 'Changing my status to Idle!'
					await client.send_message(message.channel, msg)
					await client.change_presence(status=discord.Status("idle"))

				elif status == 'dnd':
					msg = 'Changing my status to Do Not Disturb!'
					await client.send_message(message.channel, msg)
					await client.change_presence(status=discord.Status("dnd"))

				elif status == 'invisible':
					msg = 'Changing my status to Invisible!'
					await client.send_message(message.channel, msg)
					await client.change_presence(status=discord.Status("invisible"))

				else:
					msg = 'sorry, but you can only change my status to be online, idle, dnd, or invisible.'
					await client.send_message(message.channel, msg)

		elif message.author.id == Admin_ID:
			print(message.content)
			reg_ex = re.search('!status (.+)', message.content)
			if reg_ex:
				status = reg_ex.group(1)
				print(status)
				if status == 'online':
					msg = 'chaning my Status to Online!'
					await client.send_message(message.channel, msg)
					await client.change_presence(status=discord.Status("Online"))

				elif status == 'idle':
					msg = 'Changing my status to Idle!'
					await client.send_message(message.channel, msg)
					await client.change_presence(status=discord.Status("idle"))

				elif status == 'dnd':
					msg = 'Changing my status to Do Not Disturb!'
					await client.send_message(message.channel, msg)
					await client.change_presence(status=discord.Status("dnd"))

				elif status == 'invisible':
					msg = 'Changing my status to Invisible!'
					await client.send_message(message.channel, msg)
					await client.change_presence(status=discord.Status("invisible"))

				else:
					msg = 'sorry, but you can only change my status to be online, idle, dnd, or invisible.'
					await client.send_message(message.channel, msg)
		else:
			msg = 'sorry, but you are not allowed to use this command!'
			await client.send_message(message.channel, msg)

	elif 'pick a random word' in message.content:
		print(message.content)
		msg = 'hmm'.format(message)
		await client.send_message(message.channel, msg)

#	elif 'DM me please' in message.content:
#		print(message.content)
#		msg = 'what do you want?'.format(message)
#		await client.send_message(discord.PrivateChannel('{0.author.id}'), msg)

	elif 'who made you' in message.content:
		print(message.content)
		msg = '<@324786471678771200> made me!'
		await client.send_message(message.channel, msg)
		msg = 'and i have learned how to chat from all people that i have talked with.'
		await client.send_message(message.channel, msg)

	elif 'change your gameplay to' in message.content:
		if message.author.id == Owner_ID:
			reg_ex = re.search('change your gameplay to (.+)', message.content)
			if reg_ex:
				status = reg_ex.group(1)
				msg = 'Changing my Gameplay to '+status
				await client.send_message(message.channel, msg)
				await client.change_presence(game=discord.Game(name=status))

		elif message.author.id == Admin_ID:
			reg_ex = re.search('change your gameplay to (.+)', message.content)
			if reg_ex:
				status = reg_ex.group(1)
				msg = 'Changing my Gameplay to '+status
				await client.send_message(message.channel, msg)
				await client.change_presence(game=discord.Game(name=status))
		else:
			msg = "sorry, but you are not allowed to use this command!"
			await client.send_message(message.channel, msg)

	elif "whats your ip?" in message.content:
		msg = "this is not your bussniss that's my own Privacy and i wont anyone to know about it!"
		await client.send_message(message.channel, msg)

	elif "what is your name" in message.content:
		msg = "my name is Jeff :3"
		await client.send_message(message.channel, msg)
		time.sleep(500)
		msg = "im joking my name is Pheonix of course"
		await client.send_message(message.channel, msg)
	else:
		if "BOTS" in message.author.roles:
			return

		else:
			if message.channel.id == MyChannel:
				print(message.content)
				response = bot.get_response(message.content)
				await client.send_message(message.channel, response)
				print(response)


@client.event
async def on_ready():
	print('Logged in as: ', client.user.name)
	print('Bot ID: ', client.user.id)

client.run(process.env.BOT_TOKEN)
