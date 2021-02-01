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
            output = client.get_channel(427809865281437696)
            await output.send(f"**ID:** {message.author.id}\n**Name:** {message.author.name}#{message.author.discriminator}\n**Nick:** {message.author.nick}\n**Channel:** {message.channel}\n >>> {message.content}")

client = MyClient()
client.run(token)
