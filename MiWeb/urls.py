from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', include('MisPerris.urls')),
    path('admin/', admin.site.urls),
    #path('^login/$', auth_views.login, name='login'),
    #path('^logout/$', auth_views.logout, name='logout'),
]
