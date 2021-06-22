from django.db import models


class Features(models.Model):
    name = models.CharField(max_length=255)
    contact = models.IntegerField()
    interest = models.CharField(max_length=255)




