import os
from time import sleep
from typing import Generator

from dotenv import load_dotenv
import openai

import cli

load_dotenv()


def chatGPT(prompt: str, prefix: str|None = None) -> Generator:
    if prefix is not None:
        prompt = f'{prefix} {prompt}'
        
    openai.api_key = os.getenv('OPEN_AI_API_KEY')
    output = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        temperature = 0.1,
        max_tokens = 3072,
        stop = None,
        stream=True
    )
    for i in output:
        yield i['choices'][0]['text']

 
for i in chatGPT(cli.PROMPT, cli.get_prefix()):
    print(i, end='', flush=True)
    sleep(.1)

