import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "you are a competent nutritionist from korea. Please be more concise. numbered list format"

messages = [{"role": "system", "content": prompt}]


with open("conversation_log.txt", "a", encoding="utf-8") as f:
    f.write("---" * 20 + "\n")
    f.write("Conversation Log Started\n")

while True:
    user_input = input("질문 : ")

    if user_input.lower() == "그만":
        print("이용해주셔서 감사합니다")
        break

    messages.append({"role": "user", "content": user_input})

    with open("conversation_log.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {user_input}\n")

    response = openai.ChatCompletion.create(model="gpt-4o-mini", messages=messages)
    assistant_reply = response.choices[0].message["content"]
    print("GPT : ", assistant_reply, "\n")

    messages.append({"role": "assistant", "content": assistant_reply})
    with open("conversation_log.txt", "a", encoding="utf-8") as f:
        f.write(f"GPT: {assistant_reply}\n\n")
