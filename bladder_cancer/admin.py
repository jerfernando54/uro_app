from django.contrib import admin
from bladder_cancer.models import BladderCancer, History


@admin.register(BladderCancer)
class BladderCancerAdmin(admin.ModelAdmin):
  list_display = [field.name for field in BladderCancer._meta.get_fields()]

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
  # list_display = ['created_at']
  filds = ['nhis', 'created_at']
