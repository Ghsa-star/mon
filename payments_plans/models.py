from django.db import models

class PaymentPlan(models.Model):
    plan_name = models.CharField("اسم الخطة", max_length=100)
    price = models.DecimalField("السعر", max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "خطة دفع"
        verbose_name_plural = "خطط الدفع"

    def __str__(self):
        return self.plan_name
