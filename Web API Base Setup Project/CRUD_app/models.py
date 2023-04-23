from django.db import models

# Create your models here.

class patient(models.Model):

    name = models.CharField(max_length=100)
    activty = models.CharField(max_length=50)
    age = models.IntegerField()
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name