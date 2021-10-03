from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .forms import EmployeeForm
from .models import Department, Employee


# Create your views here.
class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'


class EmployeeCreateView(CreateView):
    form_class = EmployeeForm
    template_name = 'employee_form.html'
    success_url = '/success'


def success(request, *args, **kwargs):
    return HttpResponse("New employee created successfully.")