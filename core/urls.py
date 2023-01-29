from django.urls import path
from core import views

app_name = 'core'
urlpatterns = [
    path('', views.ChatView.as_view(), name="chat")
]
