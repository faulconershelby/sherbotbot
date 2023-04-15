import os
import random
from twitchio import Message
from twitchio.ext import commands
from twitchio.errors import TwitchIOException
from dotenv import load_dotenv

# @todo: add a command to add a new command
# @todo: add a command to remove a command

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



@bot.event() 
async def event_ready():
    print(f'{os.environ["BOT_NICK"]} || online')
    print(f'user id || {bot.user_id}')

@bot.event()  #@todo: fix this event so messages are printed
async def on_message_handler(channel: str, message: Message) -> None:
  assert message.author.name is not None
  assert message.content is not None

# print messages -- might need to look into parsing the object from twitch
# @todo check twitchio docs
  message_dict = vars(message)
  for key, value in message_dict.items():
    print(f"{key}: {value}")

  if message.author.name.lower() == os.environ['BOT_NICK'].lower():
    return
  command_name = message.content.strip()
  
  print(f'@{message.author.name} executed {command_name}')
  await on_message_handler(channel, message)

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
  # @todo why no work??
  if str(message.message.content).isalpha() is False:
    sides = float(''.join([i for i in message.message.content if i.isdigit()]))

  if sides > 0:
    roll_result = random.randint(1, int(sides))
    await message.send(f'🎲 {message.author.name} rolled {roll_result} 🎲')
  else:
    await message.send(f'please use a positive number')

# @todo: add a command to list all commands
@bot.command(name='sherbot-commands')
async def sherbot_commands(message):
  # create a function that makes and returns a list of commands
  pass

# @todo: add a command to tell sun sign of user if they add their birthday
@bot.command(name= 'sun-sign')
async def sun_sign_command(message):
  # create dictionary to hold all astrological signs
  # key will be name of the sign
  # value will be a dictionary with key as month and value as list of days in that month
  # for list of days, use range()
  astrology_signs= {
    'aries': {'march': range(21, 31), 'april': range(1, 19)},
    'taurus': {'april': range(20, 30), 'may': range(1, 20)},
    'gemini': {'may': range(21, 31), 'june': range(1, 20)},
    'cancer': {'june': range(21, 30), 'july': range(1, 22)},
    'leo': {'july': range(23, 31), 'august': range(1, 22)},
    'virgo': {'august': range(23, 31), 'september': range(1, 22)},
    'libra': {'september': range(23, 30), 'october': range(1, 22)},
    'scorpio': {'october': range(23, 31), 'november': range(1, 21)},
    'sagittarius': {'november': range(22, 30), 'december': range(1, 21)},
    'capricorn': {'december': range(22, 31), 'january': range(1, 19)},
    'aquarius': {'january': range(20, 31), 'february': range(1, 18)},
    'pisces': {'february': range(19, 29), 'march': range(1, 20)}
  }
  months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

  # create a function that takes in a message and returns the user's birthday
  # if the user doesn't have a birthday, return ValueError('valid birthday pls')
  # if the user has a birthday, continue
  def get_birthday(message):
    # if message content contains a string from months and a number between (1-31)
    # store month and day in variables
    # continue
    # else return ValueError('valid birthday pls')
    # look for key in astrology_signs that matches the month variablee
    # look for value in astrology_signs that matches the day variable for that month
    # return the key and value of the astrology_signs dictionary
    pass
  # if user calls sun-sign command, return their sign with get_birthday() function
  # if user calls sun-sign command and doesn't have a birthday, return ValueError('valid birthday pls')


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

@bot.event()
async def pokemon_appears(message):
  if "pokemon" in str(message.message):
    await message.send("sherbo4Pinocchio")
  if message.author.name == "PokemonCommunityGame" and "90s" in message.message:

    await message.send("!pokecheck")

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