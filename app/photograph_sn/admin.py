from django.contrib.contenttypes.admin import (
    GenericTabularInline,
    GenericStackedInline,
    GenericInlineModelAdmin
)
from django.contrib import admin
from django.utils.html import format_html
from .models import (Photo, Country, City, Thing, ContentType)

# Register your models here.
admin.site.site_title = "Панель администратора"
admin.site.index_title = "Добро пожаловать в панель администратора!"
admin.site.site_name = "Социальная сеть"

class ContentTypeInline(GenericTabularInline):
    model = ContentType
    extra = 2 
    ct_field_name = 'content_type'
    id_field_name = 'object_id'

class CountryOptions(admin.ModelAdmin):
    model = Country
    inlines = (ContentTypeInline,)

class CityOptions(admin.ModelAdmin):
    model = City
    inlines = (ContentTypeInline,)

class ThingOptions(admin.ModelAdmin):
    model = Thing
    inlines = (ContentTypeInline,)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'image', 'is_approved', 'image_tag', 'types_list')  # 'types_list'
    filter_horizontal = ('types',)

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.image.url))

    def types_list(self, obj):
        return [
            "{}: {}".format(
                x.content_object.__class__.__name__,
                x.content_object.name
            ) for x in obj.types.all()
        ]

for tpl in (
    (Photo, PhotoAdmin),
    (Country,),
    (City,),
    (Thing,),
):
    if len(tpl) > 1:
        admin.site.register(tpl[0], tpl[1])
    else:
        admin.site.register(tpl)