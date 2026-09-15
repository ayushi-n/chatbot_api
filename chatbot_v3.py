import os
from openai import OpenAI
code = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)
prompt = input("Enter your prompt: ")
system_prompt = "You are a helpful assistant that translates English to French."

response = code.responses.create(
    input = prompt,
    instructions = system_prompt,
    model="openrouter/free",
)
print(response.output_text)