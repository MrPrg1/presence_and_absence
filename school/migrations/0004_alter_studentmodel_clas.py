# Generated by Django 4.2.7 on 2023-11-05 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_classmodel_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='clas',
            field=models.ForeignKey(blank=True, help_text='کلاس خود را انتخاب نمایید', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clas', to='school.classmodel'),
        ),
    ]
