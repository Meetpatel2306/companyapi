from django.contrib import admin
from api.models import company,employee

# Register your models here.

class companyadmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)

class employeeadmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)
admin.site.register(company,companyadmin)
admin.site.register(employee,employeeadmin)