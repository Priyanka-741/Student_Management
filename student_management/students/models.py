from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=30)
    Roll_Number=models.IntegerField(unique=True)
    Age=models.IntegerField()
    Grade=models.CharField(max_length=2)

    def __str__(self):
        return self.Name