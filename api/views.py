from django.shortcuts import render,redirect
from .models import Employee 
from .serializer import EmployeeSerialzer
from rest_framework import viewsets

# Create your views here.

class Employee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialzer

