from django.urls import path, include
from core import views
from config import settings
from django.conf.urls.static import static

app_name = 'core'
urlpatterns = [
    path('', views.ChatView.as_view(), name="chat")
]

if settings.DEBUG:
    media_urls = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += media_urls
