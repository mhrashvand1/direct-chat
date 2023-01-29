from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (
    PermissionsMixin, 
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from common.models import BaseModel, UUIDBaseModel
from account.utils import get_avatar_path
from account.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin, UUIDBaseModel):

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = 'User'

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        db_index=True,
    )  
    name = models.CharField(_("name"), max_length=150)
    blockings = models.ManyToManyField(
        to='User', related_name='blockers', through='activity.Block'
    )   
    
    email = models.EmailField(_("email address"), blank=True)  
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name"]

    def __str__(self) -> str:
        return str(self.username)
    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = "%s" % (self.name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        return super().save(*args, **kwargs)


class Profile(BaseModel):
    
    class Meta:
        db_table = 'Profile'
        verbose_name = _('profile')
        verbose_name_plural = _('profile')
    
    user = models.OneToOneField(
        to='User', primary_key=True, db_index=True, 
        on_delete=models.CASCADE, related_name='profile', 
        verbose_name=_('user')
    )
    avatar = models.ImageField(
        verbose_name=_('avatar'), default='no_avatar.png',
        blank=True, upload_to=get_avatar_path
    )
    
    