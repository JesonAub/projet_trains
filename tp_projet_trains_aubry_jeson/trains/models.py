from django.db import models

# Create your models here.

class Trains(models.Model) :
    trainID = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 20)
    content = models.CharField(max_length = 2000)
    release = models.IntegerField()
    cover = models.CharField(max_length = 50)
    producer = models.CharField(max_length = 30)
    