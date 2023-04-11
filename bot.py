import os
from twitchio.ext import commands
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

@bot.event # type: ignore
async def event_ready():
    'Called once when the bot goes online.'
    print(f'{os.environ["BOT_NICK"]} is online!')
    ws = bot._ws # type: ignore
    await ws.send_msg(os.environ['CHANNEL'], f"/me has arrived, beep boop!")

    
#bot.py
if __name__ == "__main__":
    bot.run()