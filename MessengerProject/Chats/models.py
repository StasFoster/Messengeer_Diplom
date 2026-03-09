from django.db import models


class Chat(models.Model):

    name = models.TextField(null=True)
    users = models.ManyToManyField("Authtificate.UserModel", related_name="chats")
    avatar = models.ImageField(null=True)
    


class Massage(models.Model):

    author = models.ForeignKey("Authtificate.UserModel", related_name="messages", on_delete=models.CASCADE)
    chat = models.ForeignKey("Chats.Chat", related_name="messages", on_delete=models.CASCADE)

    