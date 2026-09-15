import os

from openai import OpenAI

code = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

response = code.responses.create(
    input = "Hello, how are you?",
    model="gpt-5-mini",
)

print(response.output_text)