import os

from groq import Groq

client = Groq(
    api_key='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',
)
dish = input('Enter the dish name: ')
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": f"Give me the recipe for {dish}",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)