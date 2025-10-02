from django.contrib import admin
from .models import PaymentPlan

@admin.register(PaymentPlan)
class PaymentPlanAdmin(admin.ModelAdmin):
    list_display = ("plan_name", "price")
