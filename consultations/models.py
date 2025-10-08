from django.db import models
from cloudinary.models import CloudinaryField

class Consultation(models.Model):
    title = models.CharField("عنوان الاستشارة", max_length=200)
    image = CloudinaryField("صورة الاستشارة", folder="consultations_images", blank=True, null=True)

    class Meta:
        verbose_name = "استشارة"
        verbose_name_plural = "الاستشارات"

    def __str__(self):
        return self.title
