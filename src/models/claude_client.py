import anthropic
import os

class claudeClient:
    def __init__(self):
        self.api_key= os.getenv("CLAUDE_API_KEY")
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def generate_response(self,prompt:str,model:str="claude-2",max_tokens:int =500)->str:
        res= self.client.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens_to_sample=max_tokens
        )
        return res.content[0].text