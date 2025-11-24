from openai import OpenAI

import os


print(os.getenv("OPENAI_BASE_URL"))


client = OpenAI()

completion = client.chat.completions.create(
    model= "gpt-4o",
    messages=[
        {"role": "system", "content": "assistant"},
        {"role": "user", "content": "Hello"},
    ]
)

print(completion.choices[0].message.content)


