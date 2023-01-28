from django.shortcuts import render, HttpResponse
from django.views import View


class ChatView(View):
    
    def get(self, request, *args, **kwargs):
        return HttpResponse("Wellcome to chat.(temporary.)")
