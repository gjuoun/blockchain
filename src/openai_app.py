from typing import List, Optional
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

def save_to_json(conversation: List[dict], filename: str = "chat_history.json"):
    """Save the conversation to a JSON file"""
    try:
        # Try to load existing data
        with open(filename, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist or is empty, start new list
        data = []
    
    # Append new entry
    entry = {
        "timestamp": datetime.now().isoformat(),
        "conversation": conversation
    }
    data.append(entry)
    
    # Write back to file
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

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
    # Store conversation with both user and AI messages
    conversation = [
        {"role": "user", "content": "Hello!"}
    ]
    full_response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            full_response += content
    
    # Add AI response to conversation
    conversation.append({"role": "assistant", "content": full_response})
    
    # Save the complete conversation to JSON
    save_to_json(conversation)



if __name__ == "__main__":
    client = main()
    
