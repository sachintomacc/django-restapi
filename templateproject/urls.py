
from django.contrib import admin
from django.urls import path, include
from core.views import PostView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', PostView.as_view(), name='home'),
    path('rest-auth/', include('rest_auth.urls')),
]
