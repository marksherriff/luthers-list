from django.urls import path
from . import views

urlpatterns = [
    path('loadapi/', views.load_api, name='load_api'),
]