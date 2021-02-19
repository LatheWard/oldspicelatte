from django.db import models

# Create your models here.
class Post(model.Models):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    text = models.TextField()