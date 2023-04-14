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

@bot.command(name='hello')
async def say_hello(message):
    await message.send(f' sherbo4Catscream Hello, {message.author.name} <3!')

@bot.command(name='dice')
async def roll_dice(message):
  # remove characters from the message that aren't numbers
  print('***MESSGE***', message)
  print('message.message', message.message.content)
  
  if True: 
    sides = 6

  if str(message.message.content).isalpha() is False:
    sides = float(''.join([i for i in message.message.content if i.isdigit()]))

  if sides > 0:
    roll_result = random.randint(1, int(sides))
    await message.send(f'🎲 {message.author.name} rolled {roll_result} 🎲')
  else:
    await message.send(f'please use a positive number')

@bot.command(name='subraid')
async def subraid(message):
  await message.send("sherbo4Figaroscreams sherbo4Catscream sherbo4Awoooo sherbo4Hype :sparkles: :lotus: sherbo4Love MercyWing1 sherbo4Pinocchio SHERBOT :rotating_light: RAID sherbo4Pinocchio MercyWing2 sherbo4Love :lotus: :sparkles: sherbo4Hype sherbo4Awoooo sherbo4Catscream sherbo4Figaroscreams")

@bot.command(name="pinocchio")
async def pinocchio_emote(message):
  await message.send("sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio sherbo4Awoooo sherbo4Pinocchio")

@bot.command(name="hype")
async def hype_emote(message):
  await message.send("sherbo4Catscream ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Hype ✨ sherbo4Catscream")

@bot.command(name="love")
async def love_emote(message):
  await message.send("sherbo4Sherbot <3 KPOPlove <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 sherbo4Love <3 KPOPlove <3 sherbo4Sherbot ")

@bot.command(name="figaro")
async def figaro_emote(message):
  await message.send("sherbo4Catscream sherbo4Fig sherbo4Figaroscreams sherbo4Fig sherbo4Figaroscreams sherbo4Fig sherbo4Figaroscreams 🌸🌸🌸 sherbo4Fig sherbo4Figaroscreams sherbo4Fig sherbo4Figaroscreams sherbo4Fig sherbo4Figaroscreams sherbo4Catscream")

@bot.command(name='test')
async def test(message):
  await message.send('test passed!')

bot.event(event_ready) # type: ignore
bot.event(on_message_handler) # type: ignore


#bot.py
try:
    if __name__ == "__main__":
        bot.run()
except TwitchIOException as e:
    print(e)