from django.urls import include, path
from rest_framework.routers import DefaultRouter

from employees import views

router = DefaultRouter()
router.register('document', views.DocumentViewSet)
router.register('area', views.AreaViewSet)
router.register('sub_area', views.SubAreaViewSet)
router.register('employee', views.EmployeeVewSet)

app_name = 'employees'
urlpatterns = [
    path('', include(router.urls)),
]
