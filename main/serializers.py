from rest_framework import serializers

from .models import Employee, Department, Position


class EmployeeSerializer(serializers.ModelSerializer):
    manager = serializers.HyperlinkedRelatedField(view_name='users-detail', read_only=True)
    department = serializers.HyperlinkedRelatedField(view_name='departments-detail', read_only=True)
    position = serializers.StringRelatedField(many=True)

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'manager', 'department', 'position')


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
