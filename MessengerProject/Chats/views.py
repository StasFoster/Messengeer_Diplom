from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import CreateChatForm, CreateChatUserForm
# Create your views here.

class MainPage(View):
    def get(self, request):
        user = request.user
        chats = []
        if user.is_authenticated:
            chats = user.chats.all()

        create_chat_form = CreateChatForm()
        create_user_chat_form = CreateChatUserForm()
        

        data = {
            "chats": chats,
            "create_chat_form": create_chat_form,
            "create_user_chat_form": create_user_chat_form
        }

        return render(request, "Chats/index.html", data)
    
