from django.db import models
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length = 200, unique=True)
    logo = models.ImageField(upload_to = "logos/", null=True, default=None)
    webpage = models.URLField(null=True)
    about = models.CharField(max_length = 1000)

    class Meta:
        verbose_name_plural = "Companies"

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

    class Meta:
        verbose_name_plural = "Agencies"

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
    sal_types = (
        ('H', 'per hour'),
        ('M', 'monthly'),
    )
    salary_type = models.CharField(
        max_length=1,
        choices=sal_types,
        default='M',
    )
    min_salary = models.PositiveIntegerField(default=0)
    max_salary = models.PositiveIntegerField(default=0)
    publication_date = models.DateTimeField(auto_now_add = True)
    expiration_date = models.DateField(null=True, default=None)
    must_have = models.ManyToManyField('Tag')
    nice_to_have = models.CharField(max_length = 1000)
    duties = models.CharField(max_length = 1000)
    benefits = models.CharField(max_length = 1000)
    about = models.TextField(null=True)

    def __str__(self):
        return self.position + ', ' + self.agency.company.name

    '''def get_absolute_url(self):
        return reverse('offerts:application_form')'''

class Application(models.Model):
    offert = models.ForeignKey(Offert, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(null=True)
    cv = models.FileField(upload_to = "cvs/", null=True, default=None)
    portfolio_link = models.URLField(null=True)
    message = models.TextField(null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name +", " + self.offert.position

    def get_absolute_url(self):
        return reverse('offerts:index')

class CustomQuestion(models.Model):
    offert = models.ForeignKey(Offert, on_delete=models.CASCADE)
    question = models.CharField(max_length = 500)
    answer_types = (
        ('T', 'text'),
        ('R', 'single-choice'),
        ('C', 'multiple-choice'),
    )
    answer_type = models.CharField(
        max_length=1,
        choices=answer_types,
        default='T',
        null = True
    )
    #choices for radio and checkbox lists, coma separated
    answer_choices =  models.TextField(null = True)

    def get_answers(self):
        all_answers = list(self.answer_choices.split("|"))
        del all_answers[len(all_answers)-1]
        return all_answers

    def __str__(self):
        return self.question

class CustomAnswer(models.Model):
    question = models.ForeignKey(CustomQuestion, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    answer_types = (
        ('T', 'text'),
        ('R', 'single-choice'),
        ('C', 'multiple-choice'),
    )
    answer_type = models.CharField(
        max_length=1,
        choices=answer_types,
        default='T',
        null = True
    )
    answer = models.TextField(null = True)

    def get_answers(self):
        all_answers = list(self.answer.split("|"))
        if self.answer_type == 'C':
            del all_answers[len(all_answers)-1]
        return all_answers

    def __str__(self):
        return self.question.question
