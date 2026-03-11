from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .forms import CreateChatForm
from Authtificate.models import UserModel
import json
# Create your views here.

class MainPage(View):
    def get(self, request):
        user = request.user
        chats = []
        if user.is_authenticated:
            chats = user.chats.all()

        create_chat_form = CreateChatForm()
        

        data = {
            "chats": chats,
            "create_chat_form": create_chat_form,
        }

        return render(request, "Chats/index.html", data)
    
class SearchUser(View):
    def get(self, request):
        query = request.GET.get("q")
        users = []
        if query:
            users = UserModel.objects.filter(username__icontains=query).values("id", "username")

        data = {
            "users": list(users)
        }
        return JsonResponse(data)
    

    