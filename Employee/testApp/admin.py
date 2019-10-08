from django.contrib import admin
from testApp.models import Employee
# Register your models here.
class employeeAdmin(admin.ModelAdmin):
    list_display=['empNo','empName','empSal','empAdd']

admin.site.register(Employee,employeeAdmin)
