from django.db import models

class Consultation(models.Model):
    title = models.CharField("عنوان الاستشارة", max_length=200)
    scheduled_date = models.DateTimeField("تاريخ ووقت الموعد")
    image = models.ImageField("صورة الاستشارة", upload_to="consultations_images/", blank=True, null=True)

    class Meta:
        verbose_name = "استشارة"
        verbose_name_plural = "الاستشارات"

    def __str__(self):
        return self.title
