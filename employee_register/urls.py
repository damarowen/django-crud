from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.employee_form), # employee/ , get and post req. for insert operation
    path('list/',views.employee_list) # get req. to retrieve and display all records
]