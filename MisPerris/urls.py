from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacto/', views.contacto, name='contacto'),
    path('servicios/', views.servicios, name='servicios'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
]

#wear aquí pls -> https://www.django-rest-framework.org/