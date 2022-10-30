from django.shortcuts import render
from photograph_sn.models import (
    Photo, City, Country, Thing, ContentType
)
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from .serializers import (
    ContentTypeSerializer, PhotoSerializer,
    ThingSerializer, CountrySerializer, CitySerializer,
)
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 30

class AbstractReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = None
    queryset = None
    filter_backends = (SearchFilter, OrderingFilter)
    ordering_fields = ("pk", "user", "image", "types")
    pagination_class = StandardResultsSetPagination

class AbstractViewset(viewsets.ModelViewSet):
    serializer_class = None
    queryset = None
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter)
    ordering_fields = ("pk", "user", "image", "types")
    pagination_class = StandardResultsSetPagination

class PhotoModelViewset(AbstractViewset):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.prefetch_related('types').all()
    ordering_fields = (
        "pk", "user", "image", "types"
    )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
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
