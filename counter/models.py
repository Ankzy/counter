from django.db import models


class User(models.Model):
    tg = models.IntegerField(unique=True)

class Place(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)