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
            print("1")
            output = client.get_channel(427809865281437696)
            print("2")
            await output.send(f"<@{message.author.id}> {message.author.name}#{message.author.discriminator}: {message.content}")
            print("3")

client = MyClient()
client.run(token)