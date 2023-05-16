import unittest
from unittest.mock import AsyncMock, patch
from bot import *


#go through code to test all functions

# event: event_ready()

# event: on_message_handler() 

# command: say_hello()

# command: roll_dice()

# command: flip_coin()

# command(sherbotbot)

#commands: sun_sign_command()

#commands: draw_card()
class TestDrawCard(unittest.IsolatedAsyncioTestCase):
    
    async def test_draw_card(self):
      # test for expected card
      mock_message = AsyncMock()
      with patch('bot.random.choice', return_value ='Sherbot drew The Fool'):
        await draw_card(mock_message)
      mock_message.send.assert_called_once_with('The Fool')

      # test for user's name contained in message sent
      mock_message = AsyncMock()
      mock_message.author.name = "Sherbot"
      with patch('bot.random.choice', return_value ='The Magician'):
        await draw_card(mock_message)
      mock_message.send.assert_called_once_with('Sherbot drew the Magician')

      # test that the drawn card is from the tarot deck
      mock_message = AsyncMock()
      with patch('bot.random.choice', side_effect=Exception('invalid card')):
        with self.assertRaises(Exception):
          await draw_card(mock_message)
