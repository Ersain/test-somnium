from django.urls import path

from main.views import (EmployeeListView, EmployeeDetailView, DepartmentDetailView, DepartmentListView,
                        PositionDetailView, PositionListView)

urlpatterns = [
    path('<int:pk>/', EmployeeDetailView.as_view(), name='users-detail'),
    path('', EmployeeListView.as_view(), name='users-list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='departments-detail'),
    path('departments/', DepartmentListView.as_view(), name='departments-list'),
    path('positions/<int:pk>/', PositionDetailView.as_view(), name='positions-detail'),
    path('positions/', PositionListView.as_view(), name='positions-list'),
]
