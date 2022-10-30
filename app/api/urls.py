from rest_framework.routers import DefaultRouter
from api import views


api_router = DefaultRouter()
api_router.register('photo', views.PhotoModelViewset)
api_router.register('content_types', views.ContentTypeViewset)
api_router.register('countries', views.CountryViewset)
api_router.register('cities', views.CityViewset)
api_router.register('things', views.ThingViewset)
