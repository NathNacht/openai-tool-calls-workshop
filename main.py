import json
import os
from pprint import pprint

from dotenv import load_dotenv
from openai import OpenAI

# TODO: Import google_search function or create your custom function in the utils folder and import it here
from utils.google import google_search

# Load the environment variables
load_dotenv()

# TODO: Initialize the OpenAI client
print("Initializing Client:")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEYS"), project=os.environ.get("OPENAI_PROJECT_ID"))

# TODO: Define the initial messages
print("Initializing messages:")
messages = [
    {"role": "system", "content": "You are kind assistant, u have a tool to look up stuff on google, "
                                  "use it to improve the answers you give."},
    {"role": "user", "content": "What is the latest version of python?"},
]

# TODO: define your tools specifications
tools = [
    {
        "type": "function",
        "function": {
            "name": "google_search",
            "description": "Sends a query to google to search for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "q": {
                        "type": "string",
                        "description": "The search query to search for on google",
                    },
                },
                "required": ["q"],
            },
        }
    }
]

# TODO: Make the request to openai, use the model "gpt-3.5-turbo"
print("Making the first request:")
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    tools=tools,
    temperature=0,
)

# TODO: Verify the response
print("The response of the initial request is:")
print(response.choices[0].message)

# TODO: If there is a function call than append the function call message to the messages list.
print("Appending function call message:")
messages.append(response.choices[0].message)

# TODO: Loop over the functions calls and call the functions and append the result of the functions to the list
print("Calling custom function and appending to message list:")
for tool_call in response.choices[0].message.tool_calls:  # iterate over the tool calls
    if tool_call.function.name == "google_search":  # if the tool call is for the to_the_power function
        kwargs = tool_call.function.arguments  # extract the arguments
        kwargs = json.loads(kwargs)  # convert the arguments to a dictionary
        result = google_search(**kwargs)  # call the function with the arguments **unpacks the dictionary
        call_id = tool_call.id  # extract the call id
        # append the result as a message to the message list
        # print(len(str(result)))
        messages.append({
            "role": "tool",
            "tool_call_id": call_id,
            "name": tool_call.function.name,
            "content": str(result)
        })

# TODO: Print the messages list for debugging purposes
print("The messages list before we send it to openai")
pprint(messages)

# TODO: Make the request with the updated messages list
print("Making the second request:")
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0,
)

# TODO: Verify the response
print("The response of the request is:")
print(response.choices[0].message)

# TODO: Print the resulting message!
print("The clean message reply is:")
print(response.choices[0].message.content)