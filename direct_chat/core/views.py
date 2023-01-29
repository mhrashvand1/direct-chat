from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse


class ChatView(View):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(
                reverse("account:login") + "?redirect_url=core:chat"
            )
        return super().dispatch(request, *args, **kwargs)

    
    def get(self, request, *args, **kwargs):
        return render(request, 'core/chat.html')