from django.db import models

class Consultation(models.Model):
    title = models.CharField(max_length=200)
    scheduled_date = models.DateTimeField()

    def __str__(self):
        return self.title
