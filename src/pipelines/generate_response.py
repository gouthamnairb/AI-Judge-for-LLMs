import json
from src.models.gemini_client import GeminiClient
from src.models.openai_client import OpenAIClient


def load_prompts(file_path: str):
    prompts = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            prompts.append(json.loads(line))
    return prompts


def main():
    prompts = load_prompts("data/prompts.jsonl")
    openai_client = OpenAIClient()
    gemini_client = GeminiClient()

    results = []

    for prompt_obj in prompts:
        prompt_id = prompt_obj.get("id")
        task_type = prompt_obj.get("task_type")
        prompt = prompt_obj.get("prompt")

        if not prompt:
            continue

        responses = {
            "openai": openai_client.generate_response(prompt),
            "gemini": gemini_client.generate_response(prompt),
        }

        results.append({
            "id": prompt_id,
            "task_type": task_type,
            "prompt": prompt,
            "responses": responses,
        })

    # Save results once after processing all prompts
    with open('data/model_responses.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()

    