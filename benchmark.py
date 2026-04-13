import ollama
import time

MODELS = ["llama3.2", "phi4-mini", "qwen3.5:9b"]

MODEL_INFO = {
    "llama3.2":   {"size": "2 GB", "params": "3B"},
    "phi4-mini":  {"size": "3 GB", "params": "4B"},
    "qwen3.5:9b": {"size": "6.6 GB", "params": "9B"},
}

def run_model(model, prompt):
    start = time.time()
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    end = time.time()

    return {
        "model": model,
        "response": response["message"]["content"],
        "time": round(end - start, 2)
    }


def benchmark(prompt, models=MODELS):
    results = []
    for model in models:
        result = run_model(model, prompt)
        results.append(result)
    return results


if __name__ == "__main__":
    prompt = "Explain what overfitting is in machine learning in 2 sentences."
    results = benchmark(prompt)

    print(f"\nPrompt: {prompt}")
    print("=" * 60)
    for r in results:
        print(f"\n{r['model']} — {r['time']}s")
        print(r['response'][:200] + "...")