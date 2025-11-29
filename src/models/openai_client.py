import os
import openai

class OpenAIClient:

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate_response(self, prompt: str, model: str = "gpt-4-turbo", max_tokens: int = 500) -> str:
        res = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        return  res.choices[0].message['content']
    
        
