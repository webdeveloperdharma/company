from django.urls import path
from .views import (DepartmentListView, DepartmentDetailView,
                    EmployeeCreateView, success)


urlpatterns = [
    path('departments/list', DepartmentListView.as_view()),
    path('department/<int:pk>/', DepartmentDetailView.as_view()),
    path('employee/create', EmployeeCreateView.as_view()),
    path('success/', success, name='success'),
]
