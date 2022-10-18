from django.db import models

# Create your models here.
class Place(models.Model):
    Name=models.CharField(max_length=250)
    Image=models.ImageField(upload_to='pics')
    Desc=models.TextField()

    def __str__(self):
        return self.Name


class Team(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

