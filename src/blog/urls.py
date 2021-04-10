from django.urls import include, path
from rest_framework import routers
from .views import BlogViewSet

router = routers.DefaultRouter()
router.register('blog', BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]