from typing import List, Optional
import os
from dotenv import load_dotenv
from openai import OpenAI

def main():
    """Initialize and return the OpenAI client"""
    load_dotenv()
    # print the stream result from OpenAI client, AI!
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



if __name__ == "__main__":
    client = main()
    
