import json
from  src.models.gemini_client import GeminiClient
from src .models.openai_client import OpenAIClient


def load_prompts(file_path):

    with open(file_path, 'r') as f:
        return [json.loads(line) for line in f.readlines()]
    

def main():

    prompts=load_prompts("data/prompts.jsonl")
    openai_client=OpenAIClient()
    gemini_client=GeminiClient()

    results={}

    for prompt_obj in prompts:
        prompt= prompt_obj["prompt"]
        #generating the response and storing the results in a dictionary
        results[prompt_obj]["id"]={
            openai: openai_client.generate_response(prompt),
            gemini: gemini_client.generate_response(prompt) 
        }

         # Save results as needed to file
        with open('data/model_responses.json', 'w') as f:
            json.dump(results, f, indent=2)
            
if __name__ == "__main__":
    main()

    