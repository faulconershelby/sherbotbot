# import openai
# import os
# from dotenv import load_dotenv

# load_dotenv(override=True)


# openapi_key = os.environ['OPENAI_KEY']
# openai.api_key = openapi_key
# #function to generate response using gpt-3
# #takes in users message as input, adds formatting, sends to gpt3 using openai api
# # returns response from gpt3

# def generate_response(message):
#   prompt = f"so and so said: {message}"
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
  

# generate_response("hello")