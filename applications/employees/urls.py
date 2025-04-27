from django.contrib import admin
from django.urls import path
from .views import *

app_name = "app_worker"
urlpatterns = [
    path(
        '',
        IndexTemplateView.as_view(),
        name='index'),
    path(
        'list-all/',
         ListAllEmployee.as_view(),
         name='list_all'),
    path(
        'detail/<pk>',
        EmployeeDetailView.as_view(),
        name='detail'),
    path(
        'manage/',
        ManageEmployee.as_view(),
        name='manage'),
    path(
        'update/<pk>',
        EmployeeUpdateView.as_view(),
        name='update'
    ),
    path('manage/', ManageEmployee.as_view(),name='success'),
    path(
        'delete/<pk>',
        EmployeeDeleteView.as_view(),
        name='delete'
    ),
]