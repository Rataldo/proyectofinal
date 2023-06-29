from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


#clase MEME

# class Meme(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='media/')
#     caption = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.name} - caption: {self.caption}"


#tenia el codigo de arriba pero tuve que cambiarlo a lo de abajo ya que habia subido imagenes sin agregarle la opcion de fecha
#y no me permitia hacer nuevamente las migraciones


class Meme(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
    caption = models.CharField(max_length=100)
    upload_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.upload_date:
            self.upload_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - caption: {self.caption}"


