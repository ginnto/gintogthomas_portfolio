from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    solink=models.URLField()
    gitlink = models.URLField(default="https://github.com/ginnto")
    img=models.ImageField(upload_to='picture')

