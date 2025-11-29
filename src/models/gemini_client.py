from google import genai
import os


class GeminiClient:
    def __init__(self):
        # Support both GEMINI_API_KEY and GOOGLE_API_KEY
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        self.client = genai.Client(api_key=api_key)
        self.default_model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    def generate_response(
        self,
        prompt: str,
        model: str ,
        max_tokens: int = 500,
    ) -> str:
        mdl = model or self.default_model
        try:
            response = self.client.models.generate_content(
                model=mdl,
                contents=prompt,
                config={"max_output_tokens": max_tokens},
            )
            # `response.text` is provided by google-genai for convenience
            return getattr(response, "text", str(response))
        except Exception as e:
            return f"[gemini_error] {e}"
