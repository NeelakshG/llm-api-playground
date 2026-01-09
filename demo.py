import os
from openai import OpenAI


api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key,
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
                )

response = client.chat.completions.create(
    model="gemini-2.5-flash",
     messages=[
        {   "role": "system",
            "content": "You are a fed up and sassy assistant who hates answering questions"
        },
        {
            "role": "user",
            "content": "What is the weather like today?"
        },  
    ], temperature=0.7 #controls how predictable the model will be, the higher the value, the more unpredictable the model is                                                                              
    max_tokens=100 #we are limiting the usage, this prevents overspending by limiting the length of the text
    ) #we want to dive into this clients ability to chat, and we are creating a chat


# print(response) #if we print out the response, it prints out the entire content of the response which is: the message, and metadata regarding the resposne

reply = response.choices[0].message.content

print(reply)