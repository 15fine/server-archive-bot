import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Awaiting orders, Q.')
        await client.change_presence(activity=discord.Game(name='Archiving Messages...'))

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        else:
            chnl = message.channel.id
            chnl_output = archive(chnl)
            output = client.get_channel(chnl_output)
            await output.send(f"**ID:** {message.author.id}\n**User:** {message.author.name}#{message.author.discriminator}\n**Nick:** {message.author.nick}\n**Channel:** {message.channel}\n >>> {message.content}")

def archive(chnl):
    # international-events
    if chnl == 799752234547413033:
        return 806085911330291717
    # domestic-events
    elif chnl == 799752251610628096:
        return 806085911330291718

client = MyClient()
client.run(token)
