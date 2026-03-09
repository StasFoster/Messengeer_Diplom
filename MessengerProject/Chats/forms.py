from django import forms
from .models import Chat

class CreateChatForm(forms.ModelForm): #для создвния чата
    class Meta:
        model = Chat
        fields = ('name',)

class CreateChatUserForm(forms.ModelForm): #для того чтоб написать пользователю
    class Meta:
        model = Chat
        fields = ("users",)
        widgets = {
            "users": forms.SelectMultiple(attrs={
                "size":6
            })
        }