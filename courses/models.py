from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    price = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " | " + self.subject + " | " + self.date + " | " + self.price

class Speaker(models.Model):
    name = models.ForeignKey(Course, on_delete=models.CASCADE)
    profession = models.CharField(max_length=200)