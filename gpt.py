# sudo apt install espeak

import openai
import os
from answer import say

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv("API_KEY")

def chatGPT(question : str):
    say("Wait the answer")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "user", "content": question},
            ]
    )

    return response.get("choices")[0].get("message").get("content")