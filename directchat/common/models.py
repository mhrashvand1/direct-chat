import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("updated at"))

    class Meta:
        abstract = True


class UUIDBaseModel(BaseModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True,
        verbose_name=_("id"),
    )
    
    class Meta:
        abstract = True