from django.db import models
from users.models import CustomUser

class Book(models.Model):
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.IntegerField()
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.author