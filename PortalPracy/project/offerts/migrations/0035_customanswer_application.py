# Generated by Django 2.2 on 2019-06-13 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerts', '0034_customanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customanswer',
            name='application',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='offerts.Application'),
            preserve_default=False,
        ),
    ]
