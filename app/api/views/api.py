from django.shortcuts import render
from photograph_sn.models import (
    Photo, City, Country, Thing, ContentType
)
from rest_framework.response import Response
from api.serializers import (
    ContentTypeSerializer, PhotoSerializer,
    ThingSerializer, CountrySerializer, CitySerializer,
)

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from ._base import AbstractReadOnlyViewset, AbstractViewset


# Create your views here.
class PhotoModelViewset(AbstractViewset):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.prefetch_related('types').all()
    ordering_fields = (
        "pk", "user", "image", "types"
    )

    def list(self, request, *args, **kwargs):
        get_params = request.GET
        if len(get_params) > 0:
            if 'approved' in get_params:
                if get_params['approved'].lower() == 'true':
                    queryset = self.filter_queryset(Photo.get_approved_photos())
                elif get_params['approved'].lower() == 'false':
                    queryset = self.filter_queryset(Photo.get_unapproved_photos())
            else:
                queryset_params = {}
                for param in ('country', 'city', 'thing'):
                    if param in get_params.keys():
                        if get_params[param].lower() == 'true':
                            queryset_params[param] = True
                        elif get_params[param].lower() == 'false':
                            queryset_params[param] = False
                queryset = self.filter_queryset(Photo.get_approved_photos_by_types(**queryset_params))
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ContentTypeViewset(AbstractReadOnlyViewset):
    serializer_class = ContentTypeSerializer
    queryset = ContentType.objects.all()

class CountryViewset(AbstractViewset):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class CityViewset(AbstractViewset):
    serializer_class = CitySerializer
    queryset = City.objects.all()

class ThingViewset(AbstractViewset):
    serializer_class = ThingSerializer
    queryset = Thing.objects.all()


