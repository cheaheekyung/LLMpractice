from django.shortcuts import render
from django.http import JsonResponse
from .forms import ChatForm
import openai
from dotenv import load_dotenv
import os
from .models import Chatbot
from django.contrib.auth.decorators import login_required

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "You are a competent nutritionist from Korea. Please be more concise. Numbered list format."


@login_required
def chatbot_view(request):
    form = ChatForm(request.POST or None)
    assistant_reply = None

    if request.method == "POST" and form.is_valid():
        user_input = form.cleaned_data["user_input"]

        messages = [{"role": "system", "content": prompt}]
        messages.append({"role": "user", "content": user_input})

        response = openai.ChatCompletion.create(model="gpt-4o-mini", messages=messages)
        assistant_reply = response.choices[0].message["content"]

        if request.user.is_authenticated:
            chat = Chatbot.objects.create(
                question=user_input,
                answer=assistant_reply,
            )
            chat.save()
    context = {"form": form, "assistant_reply": assistant_reply}
    return render(request, "chatbot/chatbot.html", context)
