from django.contrib.contenttypes.fields import GenericRelation
from .social_network import ContentType
from django.db import models


class CommonEntity(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    type = GenericRelation(ContentType, related_query_name='%(class)s')  # , related_query_name='%(app_label)s_%(class)s'

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.pk}: {self.name}"
    
    @classmethod
    def post_create(cls, sender, instance, created, *args, **kwargs):
        if not created:
            return
        ContentType.objects.create(content_object=instance)
