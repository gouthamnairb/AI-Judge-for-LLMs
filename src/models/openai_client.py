import os
from openai import OpenAI


class OpenAIClient:
    def __init__(self):
        # OpenAI Python SDK >= 1.x uses the OpenAI client
        api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=api_key)
        self.default_model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def generate_response(self, prompt: str, model: str | None = None, max_tokens: int = 500) -> str:
        mdl = model or self.default_model
        try:
            res = self.client.chat.completions.create(
                model=mdl,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
            )
            return res.choices[0].message.content
        except Exception as e:
            return f"[openai_error] {e}"
