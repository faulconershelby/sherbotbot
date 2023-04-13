import os
import random
from twitchio import Message
from twitchio.ext import commands
from twitchio.errors import TwitchIOException
from dotenv import load_dotenv

load_dotenv(override=True)

bot = commands.Bot(
    # set up the bot
    irc_token=os.getenv('TMI_TOKEN'),
    client_id=os.getenv('CLIENT_ID'),
    nick=os.getenv('BOT_NICK'),
    token=os.environ['BOT_TOKEN'],
    prefix=os.environ['BOT_PREFIX'],
    client_secret=os.environ['TWITCH_CLIENT_SECRET'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event  # type: ignore
async def on_message_handler(channel: str, message: Message) -> None:
  assert message.author.name is not None
  assert message.content is not None

  if message.author.name.lower() == os.environ['BOT_NICK'].lower():
    return
  command_name = message.content.strip()
  
  await bot.handle_commands(message)

  print(f'@{message.author.name} executed {command_name}')

@bot.event # type: ignore
async def event_ready():
    print(f'{os.environ["BOT_NICK"]} || online')
    print(f'user id || {bot.user_id}')

    ws = bot._ws # type: ignore

    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has arrived, beep boop!")

@bot.command(name='hello')
async def say_hello(message):
    await message.send(f'Hello, {message.author.name} <3!')

@bot.command(name='dice')
async def roll_dice(message):
    # remove characters from the message that aren't numbers
    if message.isalpha() is False:
      sides = int(''.join([i for i in message.content if i.isdigit()]))
    else:
      sides = 6
    await message.send(f' {message.author.name} rolled {random.randint(1, sides)}')

@bot.command(name='subraid')
async def subraid(message):
  await message.send("sherbo4Figaroscreams sherbo4Catscream sherbo4Awoooosherbo4Hype :sparkles: :lotus: sherbo4Love MercyWing1 sherbo4Pinocchio SHERBOT :rotating_light: RAID sherbo4Pinocchio MercyWing2 sherbo4Love :lotus: :sparkles: sherbo4Hype sherbo4Awoooo sherbo4Catscream sherbo4Figaroscreams")

@bot.command(name='test')
async def test(message):
  await message.send('test passed!')

bot.event(event_ready) # type: ignore
bot.event(on_message_handler) # type: ignore
bot.command(say_hello) # type: ignore
bot.command(roll_dice) # type: ignore
bot.command(subraid) # type: ignore
bot.command(test) # type: ignore

#bot.py
try:
    if __name__ == "__main__":
        bot.run()
except TwitchIOException as e:
    print(e)