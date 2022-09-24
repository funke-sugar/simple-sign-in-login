from django.db import models


# # Create your models here.
class Information(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
#     mobile = models.IntegerField()
#     wcode = models.CharField(max_length= 6)
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=20)

