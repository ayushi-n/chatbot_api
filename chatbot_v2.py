import os

from openai import OpenAI

code = OpenAI(
    api_key = os.environ.get("OPENROUTER_API_KEY"),
    base_url = "https://openrouter.ai/api/v1",
)
prompt = input("Enter your prompt: ")
response = code.responses.create(
    input = prompt ,
    model = "openrouter/free",
)

print(response.output_text)