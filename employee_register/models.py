from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)

#* use below, is like constructor, used for display title
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= IntegerField()
    position= models.ForeignKey(Position,on_delete=models.CASCADE)