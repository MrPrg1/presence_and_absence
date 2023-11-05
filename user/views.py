from django.shortcuts import render
from rest_framework.views import APIView
from .models import BaseUser, BaseUserSerializer
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics
from rest_framework import permissions



class TeacherView(APIView):
    permission_classes = [permissions.AllowAny]

    def get_object(self, nationalCode):
        try:
            teacher = BaseUser.objects.filter(nationalCode=nationalCode)
            return teacher
        except BaseUser.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)



    def get(self, request, nationalCode):
        teacher = self.get_object(nationalCode)
        if teacher:   
            serializer = BaseUserSerializer(teacher, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)



    def delete(self, request, nationalCode):
        teacher = self.get_object(nationalCode)
        if teacher:
            teacher.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        serializer = BaseUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.sava()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

        


    def put(self, request, nationalCode):
        teacher = self.get_object(nationalCode)
        serializer = BaseUserSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)




class AllTeacherView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        teacher = BaseUser.objects.all()
        if teacher:
            serializer = BaseUserSerializer(teacher, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
