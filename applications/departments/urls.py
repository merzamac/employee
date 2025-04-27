from django.contrib import admin
from django.urls import path
from .views import *

app_name = "app_department"
urlpatterns = [
        path(
            'department/',
            DepartmentListView.as_view(),
            name='department'),
        path(
            'bydepartment/<short_name>',
            ByDepartmentListview.as_view(),
            name='bydepartment'),
]