# Generated by Django 2.2 on 2019-04-15 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerts', '0011_offert_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offert',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
