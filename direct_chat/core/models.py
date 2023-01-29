from django.db import models
from django.contrib.auth import get_user_model
from common.models import BaseModel
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Room(BaseModel):
    
    members = models.ManyToManyField(
        to=User, 
        related_name='rooms',
        through='RoomUser',
        verbose_name='members',     
    )
    
    class Meta:
        db_table = 'Room'
        verbose_name = _('room')
        verbose_name_plural = _('rooms')
               
        
class RoomUser(BaseModel):
    
    room = models.ForeignKey(
        to='Room', 
        on_delete=models.CASCADE,
        related_name='room_user_set',      
        verbose_name='room'
    )
    user = models.ForeignKey(
        to=User, 
        on_delete=models.CASCADE,
        related_name='room_user_set',      
        verbose_name='user'
    )
    last_read = models.DateTimeField(
        default=timezone.now,
        verbose_name='last message read time'
    )
      
    class Meta:
        db_table = 'RoomUser'
        verbose_name = _('room_user')
        verbose_name_plural = _('room_user')
        unique_together = ('room', 'user')
        index_together = ('room', 'user')
           
    
class Message(BaseModel):
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE,
        related_name='messages', verbose_name='author'
    )
    room = models.ForeignKey(
        to='Room', on_delete=models.CASCADE,
        related_name='messages', verbose_name='room'
    )
    text = models.CharField(max_length=1000)
    
    class Meta:
        db_table = 'Message'
        verbose_name = _('message')
        verbose_name_plural = _('messages')
