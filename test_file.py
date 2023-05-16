import pytest
import asyncio
from bot import *

pytest_plugins = ("pytest_asyncio",)

class MockAuthor:
  def __init__(self, name):
    self.name = name

class MockMessage:
  def __init__(self, author):
    self.author = author

  
  async def send(self, message):
    pass


#write tests for bot commands

# @pytest.mark.asyncio
async def test_say_hello():
  #act
  author = MockAuthor('Sherbot')
  message = MockMessage(author=author)
  
  result = say_hello(message) # type: ignore
  #assert
  result = f' sherbo4Catscream Hello, Sherbot <3!'

