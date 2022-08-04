# System Imports
import os
from shlex import quote as os_quote
from typing import Union

# Package Imports
import openai

# Variables
first_output = "Hello, I am a chat bot. Ask me anything."
chat_log = f"{first_output}\n"
openai.api_key = "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"
completion = openai.Completion()
file = open("debug_log.txt", "w")


def openai_respond(text: str, chat_log: str) -> Union[str, str]:

    # get response from openai interface
    prompt = f"{chat_log}Human: {text}\n"
    response = completion.create(
        prompt=prompt,
        engine="davinci",
        stop=["\nHuman"],
        temperature=0.9,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        best_of=1,
        max_tokens=150,
    )

    return [response.choices[0].text.strip(), chat_log]


def respond(text: str, chat_log: str) -> Union[str, str]:
    if text == "hi":
        return ["hello, how are you?", chat_log]
    elif text == "bye":
        return ["goodbye", chat_log]
    else:
        # if response not hard coded, get the chatbot to respond
        return openai_respond(text, chat_log)


def output(text: str) -> None:
    print("\n" + text)
    os.system(f"say {os_quote(text)}")


output(first_output)

while True:
    # get some text from the user
    print("Enter some text: ")
    text = input()

    # get a response
    response_arr = respond(text, chat_log)
    response_text = response_arr[0]
    chat_log = response_arr[1]

    # output the response
    output(response_text)

    chat_log = f"{chat_log}Human: {text}\n{response_text}\n"
    file.write(chat_log)

    if text == "bye":
        file.close()
        break
