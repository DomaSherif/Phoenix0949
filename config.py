"""
This BOT was made by !MR.KIO#9581
"""

"""if anyone sends a message contains any of these words the message will be automatically removed"""
badwords = ['fuck', 'cunt', 'asshole', 'murder', 'cunt', 'dick', 'suck']
"""These are the IDs of the people that can operate the BOT (means that they can use !purge/!kick/!ban)"""
operators = [
             323699240326922240, #Adam4HD#2567
             324786471678771200  #MrKio (Even if you remove me im still inside the code ;3 )
            ]

#Feel free to replace it with your own token you can create your own by going to https://discordapp.com/developers
#after you get it you will need to invite your bot you can use https://discordapi.com/permissions.html (don't forget to get your client id)
#if you don't understand anything here is more descriptive article https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token
TOKEN = 'NjQ3NTEzODA3NzI3MzYyMDY4.Xdg0Qg.HsE97ErzxjHbobn7irKcnSUjeTU'

"""You will need to Enable  Developer Mode to get ID for the channel channel (set to None if you don't want to enable it)"""
WELCOME_MODE = "DM" #There is Different modes Options are (DM / Channel / Both) I think they explain them self. (it's not case senstive)
WELCOME_Channel_ID = 595600736969162762 #This will be requireed if set the first option with "Channel" or "Both"
DEFAULT_ROLE_ID = 593338656203472907 #This is the Role ID Anyone Joins the server will get it automatically (set it to None if you want to disable it)

#Logging Channel ID
Logging_Channel_ID = None

#Set it to False if you don't want to Allow People Sending URLs
Advertising_URLs = False

#This is the side color of them Embed
Embed_Color = 0xCC433B

BOT_PREFIX = '!'

#You can determine which part of the bot you want to enable or disable
Cogs = {'Moderation': True,
        'Debug': False,
        'Greetings': True,
        'Logger': False, #DO NOT ENABLE
        'ChatBot': True #Arificial Intelligence ChatBot
        }

#DO NOT EDIT!!!!!!!!
permissions = [['Administrator', 8],
               ['View Audit Log', 128],
               ['Manage Server', 32],
               ['Manage Roles', 268435456],
               ['Manage Channels', 16],
               ['Kick Members', 2],
               ['Ban Members', 4],
               ['Create Instant Invite', 1],
               ['Change Nickname', 67108864],
               ['Manage Nickname', 134217728],
               ['Manage Emojis', 1073741824],
               ['Manage Webhooks', 536870912],
               ['Read Messages', 1024],
               ['Send TTS Mesages', 4096],
               ['Embed Links', 16384],
               ['Read Message History', 65536],
               ['Use External Emojis', 262144],
               ['Send Messages', 2048],
               ['Manage Messages', 8192],
               ['Attach Files', 32768],
               ['Mention @everyone', 131072],
               ['Add Reactions', 64],
               ['View Channel',  1024],
               ['Connect', 1048576],
               ['Mute Members', 4194304],
               ['Move Members', 16777216],
               ['Speak', 2097152],
               ['Deafen Members', 8388608],
               ['Use Voice Activity', 33554432],
               ['Priority Speaker', 256]
               ]
