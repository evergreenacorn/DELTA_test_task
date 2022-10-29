# from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType as CT
from ._base import models, CommonEntity


# Create your models here.
class ContentType(models.Model):
    content_type = models.ForeignKey(CT, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"{self.pk}: obj=<<{self.content_object}>>"

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    types = models.ManyToManyField(ContentType)
    image = models.ImageField(upload_to="photos/%Y/%m/%d")
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pk}: {self.image.name}"

class Country(CommonEntity, models.Model):
    type = GenericRelation(ContentType)

    class Meta:
        verbose_name_plural = 'Countries'

class City(CommonEntity, models.Model):
    type = GenericRelation(ContentType)

    class Meta:
        verbose_name_plural = 'Cities'

class Thing(CommonEntity, models.Model):
    type = GenericRelation(ContentType)
