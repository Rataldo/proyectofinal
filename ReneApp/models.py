from django.db import models


# Create your models here.


class Meme(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
    caption = models.CharField(max_length=100)

    def __str__(self):
        return self.caption
