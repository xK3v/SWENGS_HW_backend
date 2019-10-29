from django.db import models

class Departement(models.Model):

    name = models.TextField()
    short_name = models.TextField(null=True)
    building = models.TextField

    def __str__(self): return self.name



class Student(models.Model):

    first_name = models.TextField()
    last_name = models.TextField()
    dob = models.DateField()
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self): return self.first_name + " " + self.last_name


