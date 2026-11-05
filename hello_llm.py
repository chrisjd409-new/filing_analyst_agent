import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

client = anthropic.Anthropic(api_key = os.getenv("anthropic_api_key"))

response = client.messages.create(
    model = "claude-sonnet-5-5",
    max_tokens = 300,
    messages = [{"role": "user", "content": "Hi tell me your name"}],

)

print(response.content[0].text)