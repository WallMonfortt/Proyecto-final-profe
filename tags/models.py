from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now=True)
    updat_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name