from django.apps import AppConfig


class PaymentsPlansConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments_plans'
    verbose_name = "خطط الدفع"
    verbose_name_plural = "إدارة خطط الدفع"
