from django.db import models

class Localisation(models.Model):
    country = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)

class Company(models.Model):
    name = models.CharField(max_length = 200)
    about = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

class Offert(models.Model):
    position = models.CharField(max_length = 50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    salary = models.IntegerField()
    must_have = models.CharField(max_length = 1000)
    nice_to_have = models.CharField(max_length = 1000)
    duties = models.CharField(max_length = 1000)
    benefits = models.CharField(max_length = 1000)
    localisation = models.CharField(max_length = 1000)

    def __str__(self):
        return self.position + ', ' + self.company.name
