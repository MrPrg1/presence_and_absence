from django.db import models
from core.models import BaseModel
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from rest_framework.serializers import ModelSerializer
# from apps.Idea.models import IdeaModel
from django.utils import timezone
class BaseUserManager(BUM):
    def create_user(self, userName, name, lastName, age, phone_number, nationalCode, dateOfBirth, degree, evidence, citizenship, email, is_active=True, is_admin=False, password=None, *args, **kwargs):

        if not phone_number:
            raise ValueError("Users must have an uniqe phone_number")

        user = self.model(
            userName=userName,
            name=name,
            lastName=lastName,
            age=age,
            phone_number=phone_number,
            nationalCode=nationalCode,
            dateOfBirth=dateOfBirth,
            degree=degree,
            evidence=evidence,
            citizenship=citizenship,
            email=email,

            is_active=is_active,
            is_admin=is_admin,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)
        return user

    def create_superuser(self, userName, name, lastName, age, phone_number, nationalCode, dateOfBirth, degree, evidence, citizenship, email, password=None, *args, **kwargs):
        user = self.create_user(
            userName=userName,
            name=name,
            lastName=lastName,
            age=age,
            phone_number=phone_number,
            nationalCode=nationalCode,
            dateOfBirth=dateOfBirth,
            degree=degree,
            evidence=evidence,
            citizenship=citizenship,
            email=email,

            is_active=True,
            is_real_estate=False,
            is_admin=True,
            password=password,
        )

        user.is_superuser = True
        user.save(using=self._db)
        return user



DEGREE_CHOICES = [
    (1, 'مدیر'),
    (2, 'معاون اموزشی'),
    (3, 'معاون فنی'),
    (4, 'هنر آموز'),
    (5, 'معاون پرورشی'),
    (6, 'معاون اموزشی'),
]

EVIDENCE_CHOICES = [
    (1, 'دیپلم'),
    (2, 'فوق دیپلم'),
    (3, 'لیسانس'),
    (4, 'فوق لیسانس'),
    (5, 'دکترا'),
]

CITIZENSHIP_CHOICES = [
            (1, 'ایرانی'),
            (2, 'تابعیت'),
        ]


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    userName = models.CharField(max_length=100, unique=True, null=False, blank=False, help_text='نام کاربری خود را وارد نمایید')
    name = models.CharField(max_length=100, help_text='نام خود را وارد نمایید')
    lastName = models.CharField(max_length=100, help_text='نام خانوادگی خود را وارد نمایید')
    age = models.IntegerField(help_text='سن خود را وارد نمایید')
    phone_number = models.IntegerField(help_text='شماره تلفن خود را وارد نمایید')
    nationalCode = models.IntegerField(help_text='شماره ملی خود را وارد نمایید')
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False, help_text='تاریخ تولد خود را وارد نمایید')
    degree = models.IntegerField(choices=DEGREE_CHOICES, help_text='سمت خود را انتخاب نمایید')
    evidence = models.IntegerField(choices=EVIDENCE_CHOICES, help_text='مدرک خود را انتخاب نمایید')
    citizenship = models.IntegerField(choices=CITIZENSHIP_CHOICES, help_text='تابعیت خود را انتخاب نمایید')
    email = models.EmailField(help_text='ایمیل خود را وارد نمایید')
    # اضافه کردن عکس

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = "userName"

    REQUIRED_FIELDS = ['name', 'lastName', 'age','phone_number', 'nationalCode', 'dateOfBirth', 'degree', 'evidence', 'citizenship', 'email']
    
    def __str__(self):
        return f"{self.name} , {self.lastName}"

    def is_staff(self):
        return self.is_admin






#serializers
class BaseUserSerializer(ModelSerializer):

    class Meta:
        model = BaseUser
        fields = ['id', 'userName', 'name', 'lastName', 'age','phone_number', 'nationalCode', 'dateOfBirth', 'degree', 'evidence', 'citizenship', 'email']








# class SocialNetworksModel(BaseModel):
#     Website = models.URLField(max_length=500)
#     Email = models.EmailField(max_length=150)
#     Eitaa = models.CharField(max_length=150)
#     Bale = models.CharField(max_length=150)
#     Rubika = models.CharField(max_length=150)
#     Soroush = models.CharField(max_length=150)
    
    
    
    
# class SocialNetworksSerializer(ModelSerializer):
#     class Meta:
#         model = SocialNetworksModel
#         fields = ['Website', 'Email', 'Eitaa', 'Bale', 'Rubika', 'Soroush']
        
        
        
        
        
        
        
        
        
        
# class AuthenticationModel(BaseModel):
#     Email = models.EmailField(max_length=254)
#     Phone = models.IntegerField()
    

          