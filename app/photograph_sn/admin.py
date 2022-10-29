from django.contrib import admin
from .models import (Photo, Country, City, Thing, ContentType)

# Register your models here.
for model in (Photo, Country, City, Thing, ContentType):
    admin.site.register(model)