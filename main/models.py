from django.db import models




class Record(models.Model):
    name = models.CharField(unique=True, max_length=150)
    email = models.CharField(unique=True, max_length=150)
    number = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return self.name






