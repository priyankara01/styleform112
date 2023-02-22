from django.db import models

# Create your models here.


class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=89)
    address = models.CharField(max_length=88)
    mail = models.EmailField()
    phone_no = models.IntegerField()
    date = models.DateField()