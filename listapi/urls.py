from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'sections', views.SectionViewSet)
router.register(r'dept/(?P<dept>.+)', views.DeptViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('loadapi/', views.load_api, name='load_api'),
    path('loadapi/<str:dept>/', views.load_api_by_dept, name='load_api_by_dept'),
    path('dept/<str:dept>/', views.find_all_by_dept, name='find_all_by_dept'),
    path('deptv2/<str:dept>/', views.find_all_by_dept_v2, name='find_all_by_dept_v2'),
]