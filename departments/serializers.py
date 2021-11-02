from rest_framework import serializers
from departments.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department_id', 'department_name', 'department_code', 'is_active']
