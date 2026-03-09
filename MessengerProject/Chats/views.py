from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main(request):
    user = request.user
    chats = []
    if user.is_authenticated:
        chats = user.chats.all()
    

    data = {
        "chats": chats,
    }

    return render(request, "Chats/index.html", data)