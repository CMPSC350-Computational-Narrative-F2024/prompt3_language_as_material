# Code to generate "poem"

#!/usr/bin/python

import os
import openai
from dotenv import dotenv_values

# Set up OpenAI credentials

CONFIG = dotenv_values(".env")

OPEN_AI_KEY = CONFIG["KEY"] or os.environ["OPEN_AI_KEY"]
OPEN_AI_ORG = CONFIG["ORG"] or os.environ["OPEN_AI_ORG"]

openai.api_key = OPEN_AI_KEY
openai.organization = OPEN_AI_ORG

def load_file(filename: str = "") -> str:
    """Loads an arbitrary file name"""
    with open(filename, "r") as fh:
        return fh.read()
    
def main():

    # Load source file
    prompt = load_file("data/prompt.txt")

    response = openai.images.generate(
        model="dall-e-3",
        prompt = prompt,
        n=1, # how many images, between 1 and 10
        #size="256x256", #dimension on the image for dall-e-2
    )

    print(response.data[0].url)
    print(response.data[0].revised_prompt)
    
if __name__ == "__main__":
    main()