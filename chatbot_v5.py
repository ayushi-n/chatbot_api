import os
from openai import OpenAI

code = OpenAI(
    api_key=os.environ.get("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)
system_prompt = "Limit your answers to one sentence."
while True:
    prompt = input("Enter your prompt: ")

    if prompt.lower() == "exit":
        print("Goodbye!")
        break

    response = code.responses.create(
        input=prompt,
        instructions=system_prompt,
        model="openrouter/free",
    )

    print(response.output_text)