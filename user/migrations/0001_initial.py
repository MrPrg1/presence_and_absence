# Generated by Django 4.2.6 on 2023-10-23 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.basemodel')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('userName', models.CharField(help_text='نام کاربری خود را وارد نمایید', max_length=100, unique=True)),
                ('name', models.CharField(help_text='نام خود را وارد نمایید', max_length=100)),
                ('lastName', models.CharField(help_text='نام خانوادگی خود را وارد نمایید', max_length=100)),
                ('age', models.IntegerField(help_text='سن خود را وارد نمایید')),
                ('phone_number', models.IntegerField(help_text='شماره تلفن خود را وارد نمایید')),
                ('nationalCode', models.IntegerField(help_text='شماره ملی خود را وارد نمایید')),
                ('dateOfBirth', models.DateField(help_text='تاریخ تولد خود را وارد نمایید')),
                ('degree', models.IntegerField(choices=[(1, 'مدیر'), (2, 'معاون اموزشی'), (3, 'معاون فنی'), (4, 'هنر آموز'), (5, 'معاون پرورشی'), (6, 'معاون اموزشی')], help_text='سمت خود را انتخاب نمایید')),
                ('evidence', models.IntegerField(choices=[(1, 'دیپلم'), (2, 'فوق دیپلم'), (3, 'لیسانس'), (4, 'فوق لیسانس'), (5, 'دکترا')], help_text='مدرک خود را انتخاب نمایید')),
                ('citizenship', models.IntegerField(choices=[(1, 'ایرانی'), (2, 'تابعیت')], help_text='تابعیت خود را انتخاب نمایید')),
                ('email', models.EmailField(help_text='ایمیل خود را وارد نمایید', max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.basemodel', models.Model),
        ),
    ]