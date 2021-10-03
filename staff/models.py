from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    department_name = models.ForeignKey("Department", on_delete=models.CASCADE, blank=True,
                                        null=True)
    email = models.EmailField(blank=True, null=True, unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.employee_name


class Department(models.Model):
    department_name = models.CharField(max_length=100, null=True, blank=True)
    manager = models.OneToOneField(Employee, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.department_name
