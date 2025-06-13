from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
import requests
load_dotenv("Chat.env")
client = InferenceClient(
    provider= os.getenv("Provider"),
    api_key= os.getenv("API_Key"),
)
prompt = input("Prompt : ")
completion = client.chat.completions.create(
    model= os.getenv("Model"),
    messages=[
        {   "role" : "system", 
            "content" : "You are an AI personal sarcastic Assistant"},
        {   "role": "user",
            "content": prompt
        }
    ],
    max_tokens=512,
)

try:
    print(completion.choices[0].message)
except ValueError:
    print("Oops out of bound")
