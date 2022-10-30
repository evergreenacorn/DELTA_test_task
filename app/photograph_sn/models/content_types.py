from ._base import models, CommonEntity
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save


class Country(CommonEntity, models.Model):
    class Meta:
        verbose_name = _("Страна")
        verbose_name_plural = _('Страны')

class City(CommonEntity, models.Model):
    class Meta:
        verbose_name = _('Город')
        verbose_name_plural = _('Города')

class Thing(CommonEntity, models.Model):
    class Meta:
        verbose_name = _('Вещь')
        verbose_name_plural = _('Вещи')


for model in (City, Country, Thing):
    post_save.connect(model.post_create, sender=model)
