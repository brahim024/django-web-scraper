from django.db import models

# Create your models here.
class Search(models.Model):
    search= models.CharField(max_length=200)
    creadet =models.DateTimeField()
    def __str__(self):
        return self.search