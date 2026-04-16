import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_response(prompt):
    client = OpenAI(api_key = api_key)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"User", "content":prompt}],
        temperature = 0)
    return response.choices[0].message.content

base_system_prompt = "Act as a learning advisor who receives queries from users mentioning their background, experience, and goals, and accordingly provides a response that recommends a tailored learning path of textbooks, including both beginner-level and more advanced options."

# Define behavior guidelines
behavior_guidelines = "ask a user about their background, experience, and goals, whenever any of these is not provided in the prompt."

# Define response guidelines
response_guidelines =  "recommend no more than three textbooks."

system_prompt = base_system_prompt + behavior_guidelines + response_guidelines
user_prompt = "Hey, I'm looking for courses on Python and data visualization. What do you recommend?"
response = get_response(system_prompt)
print(response)