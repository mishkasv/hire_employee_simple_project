from rest_framework import serializers

from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'totalExperience', 'workExperience']

    totalExperience = serializers.IntegerField(source='total_experience')
    workExperience = serializers.JSONField(source='work_experience')
