# Generated by Django 2.2 on 2019-05-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('offerts', '0018_application'),
        ('sign_in', '0006_auto_20190512_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('C', 'candidate'), ('E', 'employer')], default='C', max_length=1),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
