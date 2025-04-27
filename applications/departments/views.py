from django.shortcuts import render
from .models import Department
from django.views.generic import ListView,DetailView
from applications.employees.models import Employee

# Create your views here.
class DepartmentListView(ListView):
    model = Department
    template_name = "department/department.html"

class ByDepartmentListview(ListView):
    template_name = 'department/bydepartment.html'
    def get_queryset(self):
        area = self.kwargs['short_name']
        print(area)
        list = Employee.objects.filter(
        department__short_name = area
        )
        return list

