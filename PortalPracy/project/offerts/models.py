from django.db import models
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length = 200, unique=True)
    logo = models.ImageField(upload_to = "logos/", null=True, default=None)
    webpage = models.URLField(null=True)
    about = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

    def save(self):
        super().save()

        img = Image.open(self.logo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # resizes image (thumbnails are reduced-size versions of pictures)
            img.save(self.logo.path)

class Agency(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    country = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    weppage = models.URLField(null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.company.name + " - " + self.country + ", " + self.location

class Tag(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Offert(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length = 100)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    remote = models.BooleanField(default=False)
    per_hour = models.BooleanField("Salary: per hour", default=False)
    min_salary = models.IntegerField(default=0)
    max_salary = models.IntegerField(default=0)
    publication_date = models.DateTimeField(auto_now_add = True)
    expiration_date = models.DateField(null=True, default=None)
    must_have = models.ManyToManyField('Tag')
    nice_to_have = models.CharField(max_length = 1000)
    duties = models.CharField(max_length = 1000)
    benefits = models.CharField(max_length = 1000)
    about = models.TextField(null=True)

    def __str__(self):
        return self.position + ', ' + self.agency.company.name
# redirect link
    def get_absolute_url(self):
        return reverse('offerts:offertDetails', kwargs={'pk':self.pk})
