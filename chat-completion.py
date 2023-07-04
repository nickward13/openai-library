import os
import openai

openai.api_type = "azure"
openai.api_base = os.getenv("OPENAI_ENDPOINT")
openai.api_version = "2023-05-15"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    engine="chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Can you say something to inspire the audience of Microsoft BUILD 2023?"}
    ]
)

print(response["choices"][0]["message"]["content"])
