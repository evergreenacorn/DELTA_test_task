from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


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
