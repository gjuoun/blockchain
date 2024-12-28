from typing import List, Optional
import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    """Initialize and return the OpenAI client"""
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # Example stream request
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}],
        stream=True
    )
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")



if __name__ == "__main__":
    client = main()
    
