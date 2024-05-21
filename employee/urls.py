
from django.urls import path
from .views import EmployeeListView,EmployeeDetailView


urlpatterns = [
    path('employeeslist_create/',EmployeeListView.as_view(),name="employee"),
    path('employee/<int:pk>/',EmployeeDetailView.as_view())
]
