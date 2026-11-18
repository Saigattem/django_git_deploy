from django.contrib import admin

# Register your models here.
from hr_department.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid', 'emp_name', 'emp_salary']
    ordering = ['eid']
admin.site.register(Employee, EmployeeAdmin)