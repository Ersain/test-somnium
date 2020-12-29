from django.urls import path

from main.views import (EmployeeListView, EmployeeDetailView, DepartmentDetailView, DepartmentListView,
                        PositionDetailView, PositionListView)

urlpatterns = [
    path('<int:pk>/', EmployeeDetailView.as_view()),
    path('', EmployeeListView.as_view()),
    path('departments/<int:pk>/', DepartmentDetailView.as_view()),
    path('departments/', DepartmentListView.as_view()),
    path('positions/<int:pk>/', PositionDetailView.as_view()),
    path('positions/', PositionListView.as_view()),
]
