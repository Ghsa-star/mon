from django.db import models
from cloudinary.models import CloudinaryField  # ✅ استيراد الحقل من Cloudinary

class Consultation(models.Model):
    title = models.CharField("عنوان الاستشارة", max_length=200)
    scheduled_date = models.DateTimeField("تاريخ ووقت الموعد")
    image = CloudinaryField("صورة الاستشارة", folder="consultations_images", blank=True, null=True)  # ✅ ربط فعلي بـ Cloudinary

    class Meta:
        verbose_name = "استشارة"
        verbose_name_plural = "الاستشارات"

    def __str__(self):
        return self.title
