import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!")

snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_ready():
    print("Im Ready")

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
     await asyncio.sleep(60)
     del snipe_message_author[message.channel.id]
     del snipe_message_content[message.channel.id]

@client.command()
async def snipe(ctx):
	channel = ctx.channel
	try:
      embed = discord.Embed(
        color = discord.Color.purple()
      )
      embed.set_author(name=f"Last Deleted Message In {channel.name}")
      embed.add_field(name="Author:", value=snipe_message_author[channel.id])
      embed.add_field(name="Message:", value=snipe_message_content[channel.id])
      embed.set_footer(text="Use the help command to check out all the commands <3")
      await ctx.send(embed=embed)
	except:
      await ctx.send(f"There are no recently deleted messages in <#{channel.id}>")
    
client.run(token)
