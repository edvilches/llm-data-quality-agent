from profiler import profile_dataset
from analyzer import build_prompt
from ollama_client import ask_llm


def run_pipeline(dataset_path):

    print("[INFO] Loading dataset...")
    profile, df = profile_dataset(dataset_path)

    print("[INFO] Building prompt...")
    prompt = build_prompt(profile)

    print("[INFO] Sending request to LLM...")
    result = ask_llm(prompt)

    print("\n========== DATA QUALITY REPORT ==========\n")
    print(result)


if __name__ == "__main__":
    run_pipeline("./datasets/dirty_customers.csv")
