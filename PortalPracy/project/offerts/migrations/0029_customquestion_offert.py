# Generated by Django 2.2 on 2019-05-23 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offerts', '0028_remove_customquestion_offert'),
    ]

    operations = [
        migrations.AddField(
            model_name='customquestion',
            name='offert',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='offerts.Offert'),
        ),
    ]