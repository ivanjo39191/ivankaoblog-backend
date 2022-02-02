from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenRefreshView

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from . import serializers
from .models import Profile


class GoogleLogin(SocialLoginView):
    authentication_classes = [] # disable authentication
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.GOOGLE_OAUTH2_CALLBACKURL
    client_class = OAuth2Client

@csrf_exempt
def google_token(request):

    if "code" not in request.body.decode():
        from rest_framework_simplejwt.settings import api_settings as jwt_settings
        from rest_framework_simplejwt.views import TokenRefreshView
        
        class RefreshNuxtAuth(TokenRefreshView):
            # By default, Nuxt auth accept and expect postfix "_token"
            # while simple_jwt library doesnt accept nor expect that postfix
            def post(self, request, *args, **kwargs):
                request.data._mutable = True
                request.data["refresh"] = request.data.get("refresh_token")
                request.data._mutable = False
                response = super().post(request, *args, **kwargs)
                response.data['refresh_token'] = response.data['refresh']
                response.data['access_token'] = response.data['access']
                return response

        return RefreshNuxtAuth.as_view()(request)

    else:
        return GoogleLogin.as_view()(request)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset

    serializer_class = serializers.UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Profile.objects.filter(uid=self.request.user)
        return queryset

    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer