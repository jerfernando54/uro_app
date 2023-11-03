from django.contrib import admin
from bladder_cancer.models import BladderCancer


@admin.register(BladderCancer)
class BladderCancerAdmin(admin.ModelAdmin):
  list_display = [field.name for field in BladderCancer._meta.get_fields()]
