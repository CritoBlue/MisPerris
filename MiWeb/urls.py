from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
	path(r'', include('MisPerris.urls')),
	path('', include('pwa.urls')),
    path('admin/', admin.site.urls),
]
