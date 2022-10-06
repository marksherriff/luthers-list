from django.urls import path
from . import views

urlpatterns = [
    path('loadapi/', views.load_api, name='load_api'),
    path('dept/<str:dept>/', views.load_dept, name='load_dept'),
]