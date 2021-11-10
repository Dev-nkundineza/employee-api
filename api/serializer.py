from django.db.models import fields
from rest_framework import serializers
from .models import Employee

class EmployeeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employee

        fields = [
            
            'ename',
            'email',
            'econtact'
        ]