from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, ProfileViewSet, GoogleLogin, google_token

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),
    # path('social-login/google/', GoogleLogin.as_view(), name='google_login'),
    path('social-login/google/', google_token, name='google_login'),
]