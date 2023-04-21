import os
import re
import random
import openai
import twitchio
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

openapi_key = os.environ['OPENAI_KEY']

#function to generate response using gpt-3
#takes in users message as input, adds formatting, sends to gpt3 using openai api
# returns response from gpt3

# def generate_response(message):
#   prompt = f"{message.author.name} said: {message.message.content}"
#   response = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt=prompt,
#     max_tokens=50,
#     n=1, 
#     stop=None,
#     temperature=0.9,
#   )
#   print(f"type of response: {type(response)}")
#   print(f"value of response: {response}")

#   choices = []
#   if response.choices is not None:
#     for choice in response.choices:
#       choices.append(choice)
  
#   if len(choices) > 0:
#     return choices[0].text.strip()
#   else:
#     return "I'm sorry, I don't know how to respond to that."
  


@bot.event() 
async def event_ready():
    print(f'{os.environ["BOT_NICK"]} || online')
    print(f'user id || {bot.user_id}')

@bot.event()  #@todo: fix this event so messages are printed
async def on_message_handler(channel: str, message: Message) -> None:
  assert message.author.name is not None
  assert message.content is not None
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

#@todo integrate generate_response and gpt3
# @bot.command(name='gpt3')
# async def gpt3_response(message):
#   #ignore message sent by bot itself
#   if message.author.name.lower == os.environ['BOT_NICK'].lower():
#     return  
#   #generate response from gpt3
#   response = generate_response(message.message.content)
#   #send response to chat
#   await message.send(response)

@bot.command(name='dice')
async def roll_dice(message):
  # remove characters from the message that aren't numbers
  print('***MESSGE***', message)
  print('***message.message***', message.message.content)
  
  if True: 
    sides = 6

  if str(message.message).isalpha() is False:
    #store the numbers in message in a variable
    #convert the variable to an integer
    sides_list = []
    for i in message.message.content:
      if i.isdigit():
        sides_list.append(i)
    for j in sides_list:
      j = int(j)
    print("message numbers as list ", sides_list)
    #join strings in sides_list into 1 string
    sides = ''.join(sides_list)
    #convert joined string into an integer
    print("after converting list to single string", sides)
    if len(sides_list) == 0: 
      sides = 6
    else:
      sides = int(sides)

  if sides:
    roll_result = random.randint(1, sides)
    await message.send(f'🎲 {message.author.name} rolled {roll_result} 🎲')
  else:
    await message.send(f'please use a positive number')

@bot.command(name='coin')
async def flip_coin(message):
  flip_result = random.choice(['heads', 'tails'])
  await message.send(f'🪙 {message.author.name} flipped {flip_result} 🪙')

# @todo: add a command to list all commands
@bot.command(name='sherbotbot')
async def sherbot_commands(message):
  # create a function that makes and returns a list of commands
  pass

# @todo: add a command to tell sun sign of user if they add their birthday
@bot.command(name= 'sunsign')
async def sun_sign_command(message):
  # create a function that takes in a message and returns the user's birthday
  # if the user doesn't have a birthday, return ValueError('valid birthday pls')
  # if the user has a birthday, continue
  def get_birthday(message):
    astrology_signs= {
        'march': {'aries': range(21, 32), 'pisces': range(1, 21)},
        'april': {'taurus': range(20, 31), 'aries': range(1, 20)},
        'may': {'gemini': range(21, 32), 'taurus': range(1, 21)},
        'june': {'cancer': range(21, 31), 'gemini': range(1, 21)},
        'july': {'leo': range(23, 32), 'cancer': range(1, 23)},
        'august': {'virgo': range(23, 32), 'leo': range(1, 23)},
        'september': {'libra': range(23, 31), 'virgo': range(1, 23)},
        'october': {'scorpio': range(23, 32), 'libra': range(1, 23)},
        'november': {'sagittarius': range(22, 31), 'scorpio': range(1, 22)},
        'december': {'capricorn': range(22, 32), 'sagittarius': range(1, 22)},
        'january': {'aquarius': range(20, 32), 'capricorn': range(1, 20)},
        'february': {'pisces': range(19, 30), 'aquarius': range(1, 19)}
    }

    # months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    message_content = str(message.message.content).lower()
    words = message_content.split()[1:3]
    user_month = None
    user_day = None
    print('words', words, "message_content", message_content)

    month = words[0]
    day = words[1]
    print('month', month, 'day', day)

    user_month = month.lower().strip()
    user_day = int(day.strip(','))
    print('user_month', user_month, 'user_day', user_day)

    sign_for_month = astrology_signs[user_month]

    # if user_month and user_month not in astrology_signs:
    #   raise ValueError('invalid month')
    # if not(user_month and user_day not in astrology_signs[user_month].values()):
    #   raise ValueError('invalid day')

    for sign, day_range in sign_for_month.items():
      if user_day in day_range:
        print('sign', sign)
        return sign
    raise ValueError('valid brithday pls')
  # if user calls sun-sign command, return their sign with get_birthday() function
  # if user calls sun-sign command and doesn't have a birthday, return ValueError('valid birthday pls')
  try:
    user_sign = get_birthday(message)
    if user_sign:
      await message.send(f'Your sun sign is {user_sign.capitalize()}')
  except ValueError as e:
    print(str(e))

@bot.command(name='draw')
async def draw_card(message):
  tarot_deck = [  "The Fool",  "The Magician",  "The High Priestess",  "The Empress",  "The Emperor",  "The Hierophant",  "The Lovers",  "The Chariot",  "Strength",  "The Hermit",  "Wheel of Fortune",  "Justice",  "The Hanged Man",  "Death",  "Temperance",  "The Devil",  "The Tower",  "The Star",  "The Moon",  "The Sun",  "Judgement",  "The World",  "Ace of Wands",  "Two of Wands",  "Three of Wands",  "Four of Wands",  "Five of Wands",  "Six of Wands",  "Seven of Wands",  "Eight of Wands",  "Nine of Wands",  "Ten of Wands",  "Page of Wands",  "Knight of Wands",  "Queen of Wands",  "King of Wands",  "Ace of Cups",  "Two of Cups",  "Three of Cups",  "Four of Cups",  "Five of Cups",  "Six of Cups",  "Seven of Cups",  "Eight of Cups",  "Nine of Cups",  "Ten of Cups",  "Page of Cups",  "Knight of Cups",  "Queen of Cups",  "King of Cups",  "Ace of Swords",  "Two of Swords",  "Three of Swords",  "Four of Swords",  "Five of Swords",  "Six of Swords",  "Seven of Swords",  "Eight of Swords",  "Nine of Swords",  "Ten of Swords",  "Page of Swords",  "Knight of Swords",  "Queen of Swords",  "King of Swords",  "Ace of Pentacles",  "Two of Pentacles",  "Three of Pentacles",  "Four of Pentacles",  "Five of Pentacles",  "Six of Pentacles",  "Seven of Pentacles",  "Eight of Pentacles",  "Nine of Pentacles",  "Ten of Pentacles",  "Page of Pentacles",  "Knight of Pentacles",  "Queen of Pentacles",  "King of Pentacles"]
  card = random.choice(tarot_deck)
  await message.send(f'{message.author.name} drew {card}')
  

@bot.command(name='subraid')
async def subraid(message):
  await message.send("sherbo4FigSaroscreams sherbo4Catscream sherbo4Awoooo sherbo4Hype :sparkles: :lotus: sherbo4Love MercyWing1 sherbo4Pinocchio SHERBOT :rotating_light: RAID sherbo4Pinocchio MercyWing2 sherbo4Love :lotus: :sparkles: sherbo4Hype sherbo4Awoooo sherbo4Catscream sherbo4Figaroscreams")

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

@bot.command(name="420")
async def four_twenty_emote(message):
  await message.send("🍃 sherbo4420blaze sherbo4Towlie 💨 sherbo4420blaze sherbo4Towlie 💨 sherbo4420blaze sherbo4Towlie 💨 sherbo4420blaze sherbo4Towlie 💨 sherbo4420blaze sherbo4Towlie 💨 sherbo4420blaze sherbo4Towlie 💨 sherbo4420blaze sherbo4Towlie 🍃")

@bot.command(name="battle")
async def battle_streamraiders_url(message):
  await message.send("!battle")

@bot.command(name="addquote")
async def add_quote(message):
  await message.send("!addquote")

@bot.command(name="quote")
async def quote(message):
  await message.send("!quote")


@bot.event()
async def pokemon_appears(message):
  if "Pokemon" in str(message.message):
    await message.send("sherbo4Pinocchio")
  if message.author.name == "PokemonCommunityGame" and "90s" in message.message.content:

    await message.send("!pokecheck")

@bot.command(name='test')
async def test(message):
  await message.send('test passed!')

bot.event(event_ready) # type: ignore
bot.event(on_message_handler) # type: ignore
bot.event(pokemon_appears) # type: ignore


#bot.py
try:
    if __name__ == "__main__":
        bot.run()
except TwitchIOException as e:
    print(e)