import json
from pathlib import Path


def load_config():

    base_path = Path(__file__).resolve().parent.parent
    config_path = base_path / "config" / "config.json"

    if not config_path.exists():
        raise FileNotFoundError(
            f"Config file not found at {config_path}. "
            "Create it from config.example.json"
        )

    with open(config_path, "r") as f:
        return json.load(f)
