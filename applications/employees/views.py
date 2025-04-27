from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView,CreateView,TemplateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Employee

# Create your views here.


class IndexTemplateView(TemplateView):
    """pagina de inicio"""
    template_name = "index.html"


class ListAllEmployee(ListView):
    template_name = 'employee/list_all.html'
    paginate_by = 4
    ordering = 'first_name'

    def get_queryset(self):
        key = self.request.GET.get('kword','')
        print(key)
        list = Employee.objects.filter(
            first_name__icontains=key
        )
        return list

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = "employee/detail.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        #context['titulo'] = 'Empleado del mes'
        return context

class ManageEmployee(ListView):
    template_name = 'employee/manage.html'
    paginate_by = 6
    ordering = 'first_name'
    model = Employee

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee/update.html'
    fields = ['first_name','second_name','job','department','skills']
    success_url = reverse_lazy('app_worker:success')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(request.POST)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        return super(EmployeeUpdateView,self).form_valid(form)

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "employees/delete.html"
    success_url = reverse_lazy('persona_app:success')