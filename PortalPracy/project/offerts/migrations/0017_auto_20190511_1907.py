# Generated by Django 2.1.7 on 2019-05-11 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offerts', '0016_auto_20190511_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name_plural': 'Agencies'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
    ]
