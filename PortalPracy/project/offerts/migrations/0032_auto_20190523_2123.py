# Generated by Django 2.2 on 2019-05-23 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerts', '0031_customquestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customquestion',
            name='offert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='offerts.Offert'),
        ),
    ]