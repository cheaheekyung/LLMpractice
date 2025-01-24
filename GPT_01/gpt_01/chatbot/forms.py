from django.db import models
from django import forms


from django import forms


class ChatForm(forms.Form):
    user_input = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "질문을 입력하세요...", "rows": 4, "cols": 50}
        ),
        label="질문",
    )
