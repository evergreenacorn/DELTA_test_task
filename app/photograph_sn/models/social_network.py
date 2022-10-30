from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType as CT
from django.db import models

# Create your models here.
class ContentType(models.Model):
    content_type = models.ForeignKey(CT, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Тип контента')
        verbose_name_plural = _('Типы контента')
        indexes = [models.Index(fields=['content_type', 'object_id'])]

    def __str__(self):
        return f"{self.pk}: <<{self.content_object.__class__.__name__}: {self.content_object.name}>>"

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    types = models.ManyToManyField(ContentType)
    image = models.ImageField(upload_to="photos/%Y/%m/%d")
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Фото')
        verbose_name_plural = _('Фото')

    def __str__(self):
        return f"{self.pk}: {self.image.name}"

    # @classmethod
    # def things_photos(cls):
    #     return cls.objects.prefetch_related()
