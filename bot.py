import os
import random
from twitchio import Message
from twitchio.ext import commands
# from twitchio.client import Client
from twitchio.errors import TwitchIOException
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    token=os.environ['BOT_TOKEN'],
    prefix=os.environ['BOT_PREFIX'],
    client_secret=os.environ['TWITCH_CLIENT_SECRET'],
    initial_channels=[os.environ['CHANNEL']]
)
# opts = {
#     'identity': {
#     'username': os.environ['BOT_NICK'],
#     'password:': os.environ['TMI_TOKEN'],
#     },
#     'channels': [os.environ['CHANNEL']] # type: ignore
# }

# client = Client(**opts)

@bot.event #type: ignore
async def on_message_handler(channel: str, message: Message) -> None:
  if message.author.name.lower() == os.environ['BOT_NICK'].lower():
      return
  
  command_name = message.content.strip()

  if command_name == (f'!dice'):
    num = roll_dice()
    await message.channel.send(f'@{message.author.name} rolled a {num}')
    print(f'@{message.author.name} executed {command_name}')
  else:
    print(f'unknown command: {command_name}')

@bot.event # type: ignore
async def on_connect_handler():
    print(f'{os.environ["BOT_NICK"]} is online!')
    # ws = bot._ws # type: ignore
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has arrived, beep boop!")


def roll_dice() -> int:
    sides = 20
    return random.randint(1, sides)

bot.event(on_connect_handler) # type: ignore
bot.event(on_message_handler) # type: ignore

# client.event(on_connect_handler) # type: ignore
# client.event(on_message_handler) #type: ignore


#bot.py
try:
    # client.run()
    if __name__ == "__main__":
      bot.run()
except TwitchIOException as e:
    print(e)