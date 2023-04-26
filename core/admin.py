from django.contrib import admin

# Register your models here.

# registro do modelo de DB de models.py

from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Employee._meta.fields]


admin.site.register(Employee, EmployeeAdmin)