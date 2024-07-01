import os
import json

from dotenv import load_dotenv
from openai import OpenAI
# TODO: Import google_search function or create your custom function in the utils folder and import it here

# Load the environment variables
load_dotenv()

# TODO: Initialize the OpenAI client
print("Initializing Client:")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEYS"), project=os.environ.get("OPENAI_PROJECT_ID"))

# TODO: Define the initial messages
print("Initializing messages:")
messages = []

# TODO Define the tool specifications
tools = [

]

# TODO: Make the request to openai, use the model "gpt-3.5-turbo"
print("Making the first request:")

# TODO: Verify the response
print("The response of the initial request is:")

# TODO: If there is a function call than append the function call message to the messages list.
print("Appending function call message:")

# TODO: Loop over the functions calls and call the functions and append the result of the functions to the list
print("Calling custom function and appending to message list:")

# TODO: Print the messages list for debugging purposes
print("The messages list before we send it to openai")
print(messages)

# TODO: Make the request with the updated messages list
print("Making the second request:")

# TODO: Verify the response
print("The response of the request is:")

# TODO: Print the resulting message!
print("The clean message reply is:")
