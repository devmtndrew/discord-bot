import interactions 
import os

token = os.environ.get("TOKEN")

bot = interactions.Client(token=token)

#your server id here 
server_id = 

@bot.event
async def on_ready():
  print("Bot is ready!")

@bot.command(
  name="hello",
  description="Says hello!",
  scope=server_id
)
async def hello(ctx: interactions.CommandContext):
  await ctx.send(f"Hello, {ctx.author.mention}")

bot.start()
