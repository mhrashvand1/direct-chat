from django.contrib import admin
from core.models import Room, RoomUser, Message


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id']
    pass

@admin.register(RoomUser)
class RoomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass