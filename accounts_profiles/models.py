from django.db import models

class AccountProfile(models.Model):
    name = models.CharField("الاسم الكامل", max_length=100)
    email = models.EmailField("البريد الإلكتروني", unique=True)

    class Meta:
        verbose_name = "ملف مستخدم"
        verbose_name_plural = "ملفات المستخدمين"

    def __str__(self):
        return self.name
