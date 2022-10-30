from rest_framework.serializers import HyperlinkedModelSerializer, RelatedField
from photograph_sn.models import City, Country, Thing


class AbstractContentTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        fields = "__all__"

class ContentTypeField(RelatedField):
    def to_representation(self, value):
        if isinstance(value, Country):
            return f'Country (id: {value.id}, name: {value.name})'
        elif isinstance(value, City):
            return f'City (id: {value.id}, name: {value.name})'
        elif isinstance(value, Thing):
            return f'Thing (id: {value.id}, name: {value.name})'
        else:
            raise Exception('Unexpected type of tagged object')
