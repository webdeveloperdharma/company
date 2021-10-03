from django.contrib import admin
from .models import Employee, Department

# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_of_birth'
    list_display = ['employee_name', 'department_name', 'email', 'date_of_birth']
    list_filter = ['department_name__department_name']


class DepartmentInline(admin.StackedInline):
    model = Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    inlines = [DepartmentInline]

