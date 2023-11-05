from django.contrib import admin
from .models import StudentModel, ClassModel, PresenceAndAbsenceModel, ScoreModel
# from .models import StudentModel


@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastName', 'nationalCode', 'phoneNumber', 'fatherPhoneNumber', 'fatherName', 'homePhoneNumber', 'dateOfBirth', 'email', 'address', 'clas', 'image', 'degree']


@admin.register(ClassModel)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'studentNumber']

    


@admin.register(PresenceAndAbsenceModel)
class PresenceAndAbsenceAdmin(admin.ModelAdmin):
    list_display = ['student', 'presence', 'data']



@admin.register(ScoreModel)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['student', 'score', 'description', 'teacher']

# admin.site.register(StaffModels)


# @admin.register(StudentModel)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['user', 'presence', 'data', 'score', 'description']