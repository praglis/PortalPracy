# Generated by Django 2.2 on 2019-04-04 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='localisation',
        ),
        migrations.AddField(
            model_name='joboffert',
            name='localisation',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
    ]
