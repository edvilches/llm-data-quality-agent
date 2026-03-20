import requests
from config_loader import load_config


config = load_config()

HOST = config["ollama"]["host"]
PORT = config["ollama"]["port"]
MODEL = config["ollama"]["model"]

OLLAMA_URL = f"http://{HOST}:{PORT}/api/generate"


def ask_llm(prompt: str) -> str:
    """
    Sends a prompt to Ollama and returns the response text.
    """

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Connection error with Ollama: {e}")

    # Debug opcional (puedes dejarlo por ahora)
    print(f"[DEBUG] Status: {response.status_code}")

    if response.status_code != 200:
        raise RuntimeError(
            f"Ollama API error {response.status_code}:\n{response.text}"
        )

    data = response.json()

    if "response" not in data:
        raise RuntimeError(
            f"Invalid response from Ollama:\n{data}"
        )

    return data["response"]

