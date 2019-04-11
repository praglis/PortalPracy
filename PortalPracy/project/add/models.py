from django.db import models
from offerts.models import Offert

class Form(models.Model):
    offert = models.ForeignKey(Offert, on_delete=models.CASCADE)
    questions = models.TextField(null=True)

    def __str__(self):
        return "Application form for " + self.offert.position + " in " + self.offert.agency.company.name
