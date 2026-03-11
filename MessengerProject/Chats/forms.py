from django import forms
from .models import Chat

class CreateChatForm(forms.ModelForm): #для создвния чата
    class Meta:
        model = Chat
        fields = ('name',)

