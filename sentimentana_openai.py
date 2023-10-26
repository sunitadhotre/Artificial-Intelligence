import openai
import os

openai.api_key = "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"


#https://platform.openai.com/docs/api-reference/audio/createTranscription?lang=python
def get_response_to_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message['content']

prompt = "Classify the text below, delimited by three dashes (-), as having either a positive or negative sentiment.\nI  had a good time at Pune!  Not Learned a lot and also not made any great new friends!"


response = get_response_to_prompt(prompt)
print(response)
