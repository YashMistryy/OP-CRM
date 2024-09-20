from django.contrib import admin
from .models import Employee , Company

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ('user','department')
    
    

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display= ('name','established_date')