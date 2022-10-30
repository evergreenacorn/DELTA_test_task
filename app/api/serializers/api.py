from rest_framework.serializers import ModelSerializer
from photograph_sn.models import (
    Photo, City, Country, Thing, ContentType
)
from ._base import AbstractContentTypeSerializer, ContentTypeField
from django.db.models import Q


class CountrySerializer(AbstractContentTypeSerializer):
    class Meta(AbstractContentTypeSerializer.Meta):
        model = Country
        fields = "__all__"

class CitySerializer(AbstractContentTypeSerializer):
    class Meta(AbstractContentTypeSerializer.Meta):
        model = City
        fields = "__all__"

class ThingSerializer(AbstractContentTypeSerializer):
    class Meta(AbstractContentTypeSerializer.Meta):
        model = Thing
        fields = '__all__'

class ContentTypeSerializer(AbstractContentTypeSerializer):
    content_object = ContentTypeField(read_only=True, many=False)

    class Meta(AbstractContentTypeSerializer.Meta):
        model = ContentType
        fields = ('url', 'pk', 'object_id', 'content_type', 'content_object')

class PhotoSerializer(ModelSerializer):
    types = ContentTypeSerializer(many=True)

    class Meta:
        model = Photo
        fields = "__all__"
