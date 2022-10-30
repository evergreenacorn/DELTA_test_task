from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType as CT
from django.db import models
from django.db.models import Q

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

    @classmethod
    def get_content_countries(cls):
        return cls.objects.filter(country_name__isnull=False)

    @classmethod
    def get_content_cities(cls):
        return cls.objects.filter(city__name__isnull=False)

    @classmethod
    def get_content_things(cls):
        return cls.objects.filter(thing__name__isnull=False)

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    types = models.ManyToManyField(ContentType)
    image = models.ImageField(upload_to="photos/%Y/%m/%d")
    is_approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Фото')
        verbose_name_plural = _('Фото')

    def __str__(self):
        return f"{self.id}: {self.image.name}"

    @classmethod
    def get_approved_photos(cls):
        """Все одобренные фото"""
        return cls.objects.prefetch_related('types').filter(is_approved=True)

    @classmethod
    def get_approved_photos_by_types(cls, country=True, city=True, thing=True):
        """Все одобренные фото указанных типов"""
        approved_photos = cls.get_approved_photos()
        query = Q()
        if country:
            query &= Q(types__country__name__isnull=True)
        else:
            query &= Q(types__country__name__isnull=False)
        if city:
            query &= Q(types__city__name__isnull=True)
        else:
            query &= Q(types__city__name__isnull=False)
        if thing:
            query &= Q(types__thing__name__isnull=True)
        else:
            query &= Q(types__thing__name__isnull=False)
        return approved_photos.filter(query).distinct()

    @classmethod
    def get_unapproved_photos(cls):
        """Все неодобренные фото"""
        return cls.objects.prefetch_related('types').filter(is_approved=False)
