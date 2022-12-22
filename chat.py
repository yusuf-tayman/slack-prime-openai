import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def chat_ai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return response['choices'][0]['text']
