from django.db import models

# Create your models here.


class movies(models.Model):

    title = models.CharField(max_length = 200)
    dialogue = models.CharField(max_length = 200)
    villian = models.CharField(max_length = 200)
    year = models.IntegerField()
    rating = models.IntegerField()


    def __str__(self):
        return self.title