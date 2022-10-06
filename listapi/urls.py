from django.urls import path
from . import views

urlpatterns = [
    path('loadapi/', views.load_api, name='load_api'),
    path('loadapi/<str:dept>/', views.load_api_by_dept, name='load_api_by_dept'),
    path('dept/<str:dept>/', views.find_all_by_dept, name='find_all_by_dept'),
    path('deptv2/<str:dept>/', views.find_all_by_dept_v2, name='find_all_by_dept_v2'),
]