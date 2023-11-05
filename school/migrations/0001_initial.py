# Generated by Django 4.2.7 on 2023-11-05 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('name', models.CharField(help_text='اسم کلاس را وارد کنید', max_length=100)),
                ('studentNumber', models.IntegerField(help_text='تعداد هنرجویان کلاس را وارد کنید')),
                ('techer', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('name', models.CharField(help_text='نام خود را وارد نمایید', max_length=100)),
                ('lastName', models.CharField(help_text='نام خانوادگی خود را وارد نمایید', max_length=100)),
                ('nationalCode', models.IntegerField(help_text='شماره ملی خود را وارد نمایید', unique=True)),
                ('phoneNumber', models.IntegerField(help_text='شماره تلفن خود را وارد نمایید', unique=True)),
                ('fatherPhoneNumber', models.IntegerField(help_text='شماره تلفن پدر را وارد نمایید')),
                ('fatherName', models.CharField(help_text='نام پدر را وارد نمایید', max_length=100)),
                ('homePhoneNumber', models.IntegerField(help_text='شماره تلفن منزل را وارد نمایید')),
                ('dateOfBirth', models.DateField(help_text='تاریخ تولد خود را وارد نمایید')),
                ('email', models.EmailField(blank=True, help_text='ایمیل خود را وارد نمایید', max_length=100, null=True)),
                ('address', models.CharField(blank=True, help_text='آدرس منزل خود را وارد نمایید', max_length=500, null=True)),
                ('image', models.ImageField(blank=True, help_text='عکس خود را وارد نمایید', null=True, upload_to='imageStudents')),
                ('degree', models.IntegerField(choices=[(1, 'انظامات'), (2, 'شورا'), (3, 'معمولی')], help_text='سمت خود را انتخاب کنید')),
                ('clas', models.ForeignKey(help_text='کلاس خود را انتخاب نمایید', on_delete=django.db.models.deletion.CASCADE, related_name='clas', to='school.classmodel')),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='ScoreModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('score', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.studentmodel')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.basemodel',),
        ),
        migrations.CreateModel(
            name='PresenceAndAbsenceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence', models.IntegerField(choices=[(1, 'حاضر'), (2, 'غایب'), (3, 'تاخیر')], default=2)),
                ('data', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='school.studentmodel')),
            ],
        ),
    ]
