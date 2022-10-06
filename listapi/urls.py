from django.urls import path
from . import views

urlpatterns = [
    path('loadapi/', views.load_api, name='load_api'),
    path('olddept/<str:dept>/', views.find_all_by_dept_old, name='find_all_by_dept_old'),
    path('dept/<str:dept>/', views.find_all_by_dept, name='find_all_by_dept'),
]