from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('misperris/', include('MisPerris.urls')),
    path('admin/', admin.site.urls),
]
