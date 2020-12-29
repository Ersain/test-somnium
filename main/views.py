from rest_framework import generics

from .models import Employee, Department, Position
from .serializers import EmployeeSerializer, DepartmentSerializer, PositionSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetailView(generics.RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PositionListView(generics.ListAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionDetailView(generics.RetrieveAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
