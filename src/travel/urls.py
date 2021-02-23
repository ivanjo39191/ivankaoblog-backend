from django.urls import include, path
from rest_framework import routers
from .views import TravelViewSet,RatingViewSet, PlaceViewSet

router = routers.DefaultRouter()
router.register('travels',TravelViewSet)
router.register('ratings',RatingViewSet)
router.register('places',PlaceViewSet)


urlpatterns = [
    path('', include(router.urls)),
]