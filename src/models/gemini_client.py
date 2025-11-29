from google import genai
import os


class GeminiClient:
    def __init__(self):
        # Uses GEMINI_API_KEY (or GOOGLE_API_KEY) from environment by default
        api_key = os.getenv("GEMINI_API_KEY") 
        self.client = genai.Client(api_key=api_key)

    def generate_response(
        self,
        prompt: str,
        model: str = "gemini-2.5-flash",
        max_tokens: int = 500,
    ) -> str:
        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
            config={"max_output_tokens": max_tokens},
        )
        return response.text
