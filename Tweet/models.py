from django.db import models


class Tweet(models.Model):
    details = models.TextField()
    image = models.FileField(storage="/image")