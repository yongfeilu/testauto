from django.contrib import admin
from .models import Company

# register a model
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
