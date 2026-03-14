from profiler import profile_dataset
from analyzer import build_prompt
from ollama_client import ask_llm


def run_pipeline(dataset):

    profile, df = profile_dataset(dataset)

    prompt = build_prompt(profile)

    result = ask_llm(prompt)

    print("\nDATA QUALITY REPORT\n")
    print(result)


if __name__ == "__main__":

    run_pipeline("../datasets/dirty_customers.csv")
