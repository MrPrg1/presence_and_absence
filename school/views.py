from django.shortcuts import render
from rest_framework import generics
from .models import PresenceAndAbsenceModel, PresenceAndAbsenceSerializer, ScoreModel, ScoreSerializer, StudentModel, StudentSerializer, ClassModel, ClassSerializer
# from .models import StudentModel, StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from django.shortcuts import render
from rest_framework.views import APIView
from .models import BaseUser, BaseUserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics
from rest_framework import permissions
from django_jalali.db import models as jmodels




class AllScoreView(APIView):
    permission_classes = [permissions.AllowAny]

    # def get(self, request, sId):
    #     student = StudentModel.objects.filter(nationalCode=sId)
    #     if student:
    #         score = ScoreModel.objects.filter(student=student)
    #         if score:
    #             serializer = ScoreSerializer(score, many=True)
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         return Response(None, status=status.HTTP_404_NOT_FOUND)
    #     return Response(None, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        queryset = ScoreModel.objects.all()
        serializer = ScoreSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        queryset = ScoreModel.objects.filter(id=request['id'])
        queryset.delete()
        return Response(None, status=status.HTTP_404_NOT_FOUND)


    def put(self, request):
        queryset = ScoreModel.objects.filter(id=request['id'])
        serializer = ScoreSerializer(queryset, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)



class AllPresenceAndAbsenceView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        queryset = PresenceAndAbsenceModel.objects.all()
        serializer = PresenceAndAbsenceSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class PresenceAndAbsenceView(APIView):
    permission_classes = [permissions.AllowAny]
    def get_object(self, date):
        try:
            presenceAndAbsence = PresenceAndAbsenceModel.objects.filter(data=date)
            return presenceAndAbsence
        except PresenceAndAbsenceModel.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

    
    def get(self, request, date):
        presenceAndAbsence = self.get_object(date)
        if presenceAndAbsence:
            serializer = PresenceAndAbsenceSerializer(presenceAndAbsence, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_404_NOT_FOUND)
 

    def delete(request, data):
        presenceAndAbsence = self.get_object(date)
        if presenceAndAbsence:
            presenceAndAbsence.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(None, status=status.HTTP_404_NOT_FOUND)


    def post(self, request):
        serializer = PresenceAndAbsenceSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, date):
        presenceAndAbsence = self.get_object(date)
        serializer = PresenceAndAbsenceSerializer(presenceAndAbsence, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)





class AllStudentView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        student = StudentModel.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
     


class StudentView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, nationalCode):
        try:
            student = StudentModel.objects.filter(nationalCode=nationalCode)
            return student
        except StudentModel.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)



    def get(self, request, nationalCode):
        student = self.get_object(nationalCode)
        if student:   
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



    def delete(self, request, nationalCode):
        student = self.get_object(nationalCode)
        if student:
            student.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.sava()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

        


    def put(self, request, nationalCode):
        student = self.get_object(nationalCode)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)




class AllClassView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        clas = ClassModel.objects.all()
        if clas:
            serializer = ClassSerializer(clas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)



class ClassView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, name):
        try:
            clas = ClassModel.objects.filter(name=name)
            return clas
        except StudentModel.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)



    def get(self, request, name):
        clas = self.get_object(name)
        if clas:   
            serializer = ClassSerializer(clas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



    def delete(self, request, name):
        clas = self.get_object(name)
        if clas:
            clas.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.sava()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

        

    def put(self, request, nationalCode):
        clas = self.get_object(name)
        serializer = ClassSerializer(clas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)










