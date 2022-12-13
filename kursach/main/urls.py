from django.urls import path, include
from . import views
from .views import MyLoginView, Register

urlpatterns = [
    path('', views.index, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    path('auth/login/', MyLoginView.as_view(), name='login'),
    path('auth/', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('demo/', views.demo, name='demo'),
]