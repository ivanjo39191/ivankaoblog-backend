from django.urls import include, path
from rest_framework import routers
from .views import BlogViewSet, BlogSettingViewSet, HomeCarouselViewSet, BlogTypeViewSet

router = routers.DefaultRouter()
router.register('blog', BlogViewSet)
router.register('blogsetting', BlogSettingViewSet)
router.register('homecarousel', HomeCarouselViewSet)
router.register('blogtype', BlogTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]