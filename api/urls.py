from django.contrib import admin
from django.urls import path,include
from api.views import companyV,employeeV
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'companies',companyV)
router.register(r'employees',employeeV)
urlpatterns = [
    path('',include(router.urls)),
]
