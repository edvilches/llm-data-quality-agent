import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llm(prompt, model="llama3"):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
