import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="a!", intents=discord.Intents.all())
token = ""

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="a!", intents=discord.Intents.all())

    def run(self):
        super().run(token, reconnect=True)


@Client().event
async def on_ready():
    print('Awaiting orders, Q.')
    await client.change_presence(activity=discord.Game(name='Archiving Messages...'))

@Client().event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author.id != Client().id:
        # change the ID in the brackets to the desired output channel
        output = Client().get_channel(427809865281437696)
        await output.send(f"**ID:** {message.author.id}\n**Name:** {message.author}\n**Nick:** {message.author.display_name}\n**Channel:** {message.channel}\n >>> {message.content}")

def archive(chnl):
    # international-events
    if chnl == 799752234547413033:
        return 806085911330291717
    # domestic-events
    elif chnl == 799752251610628096:
        return 806085911330291718

Client().run(token)
