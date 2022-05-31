from django.db import models


# Create your models here.

class Flight(models.Model):
    plane_id = models.ForeignKey('Plane', on_delete=models.CASCADE)
    date = models.DateTimeField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Plane(models.Model):
    type = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.type)
