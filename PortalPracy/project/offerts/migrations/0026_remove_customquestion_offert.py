# Generated by Django 2.2 on 2019-05-23 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offerts', '0025_auto_20190523_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customquestion',
            name='offert',
        ),
    ]