"""ttime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from django.views.static import serve

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views

admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = []
urlpatterns_args = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('users.urls')),
    path('api/blog/', include('blog.urls')),
    
    url(
        r'^static/(?P<path>.*)$', serve, {
            'document_root': settings.STATIC_ROOT,
        }
    ),
    url(
        r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }
    ),
]
urlpatterns += urlpatterns_args[:]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)