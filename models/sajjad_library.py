from django.db import models


# This model is for the library of sajjad that contains the books class
# with book name, book rate and free properties.
class Book(models.Model):
    name = models.CharField(max_length=10)
    rate = models.IntegerField(default=0)
    free = models.BooleanField(default=True)
