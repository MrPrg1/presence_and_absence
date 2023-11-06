from django.db import models
from user.models import BaseUser, BaseUserSerializer
from django.utils import timezone
from core.models import BaseModel
from rest_framework.serializers import ModelSerializer
from core.models import BaseModel
from datetime import datetime
from django_jalali.db import models as jmodels





CHOICES_NAME = [
    (1, 'حاضر'),
    (2, 'غایب'),
    (3, 'تاخیر'),
]


DEGREE_CHOICES = [
    (1, 'انظامات'),
    (2, 'شورا'),
    (3, 'معمولی'),
]




class StudentModel(BaseModel):     
    name = models.CharField(max_length=100, help_text='نام خود را وارد نمایید')
    lastName = models.CharField(max_length=100, help_text='نام خانوادگی خود را وارد نمایید')
    nationalCode = models.IntegerField(unique=True, help_text='شماره ملی خود را وارد نمایید')
    phoneNumber = models.IntegerField(unique=True, help_text='شماره تلفن خود را وارد نمایید')
    fatherPhoneNumber = models.IntegerField(help_text='شماره تلفن پدر را وارد نمایید')
    fatherName = models.CharField(max_length=100, help_text='نام پدر را وارد نمایید')
    homePhoneNumber = models.IntegerField(help_text='شماره تلفن منزل را وارد نمایید')
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False, help_text='تاریخ تولد خود را وارد نمایید')
    email = models.EmailField(max_length=100, null=True, blank=True, help_text='ایمیل خود را وارد نمایید')
    address = models.CharField(max_length=500, null=True, blank=True, help_text='آدرس منزل خود را وارد نمایید')
    clas = models.ForeignKey('ClassModel', on_delete=models.CASCADE, null=True, blank=True, related_name='clas', help_text='کلاس خود را انتخاب نمایید')
    image = models.ImageField(upload_to='imageStudents', null=True, blank=True, help_text='عکس خود را وارد نمایید')
    degree = models.IntegerField(choices=DEGREE_CHOICES, help_text='سمت خود را انتخاب کنید')


    def __str__(self):
        return f'{self.name} , {self.lastName}'





class ClassModel(BaseModel):
    name = models.CharField(max_length=100, help_text='اسم کلاس را وارد کنید')
    studentNumber = models.IntegerField(help_text='تعداد هنرجویان کلاس را وارد کنید')
    techer = models.ManyToManyField(BaseUser)
    students = models.ManyToManyField(StudentModel)


    def __str__(self):
        return self.name





class PresenceAndAbsenceModel(models.Model):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE, related_name='user')
    presence = models.IntegerField(default=2, choices=CHOICES_NAME)
    data = models.DateField(auto_now=False, auto_now_add=False, default=datetime.now)
    # data = jmodels.jDateTimeField(auto_now_add=True)




class ScoreModel(BaseModel):
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    teacher = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)





class StudentSerializer(ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ['id', 'name', 'lastName', 'nationalCode', 'phoneNumber', 'fatherPhoneNumber', 'fatherName', 'homePhoneNumber', 'dateOfBirth', 'email', 'address', 'clas', 'image', 'degree']




class ClassSerializer(ModelSerializer):
    class Meta:
        model = ClassModel
        fields = '__all__'
        depth = 2




class PresenceAndAbsenceSerializer(ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = PresenceAndAbsenceModel
        fields = '__all__'
        # depth = 1




class ScoreSerializer(ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = ScoreModel
        fields = '__all__'
        # depth = 1


# class StudentModel(BaseModel):
#     user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name='user')
#     presence = models.IntegerField(default=2, choices=CHOICES_NAME)
#     data = models.DateTimeField(db_index=True, default=timezone.now)
#     score = models.IntegerField(default=0)
#     description = models.TextField(null=True, blank=True)
    

# class StudentSerializer(ModelSerializer):
#     class Meta:
#         model = StudentModel
#         fields = '__all__'
#         depth = 1
