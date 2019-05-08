from django.core.management.base import BaseCommand
from offerts.models import Company, Agency, Tag, Offert
import random

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print('Data created!')
