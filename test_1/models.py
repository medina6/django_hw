from django.db import models

class Post(models.Model):
    topic = models.CharField(max_length=55)
    meaning = models.CharField(max_length=100)

class Comment(models.Model):
    positive = models.CharField(max_length=30)
    negative = models.CharField(max_length=20)



