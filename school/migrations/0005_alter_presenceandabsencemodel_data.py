# Generated by Django 4.2.7 on 2023-11-06 00:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_studentmodel_clas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenceandabsencemodel',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
