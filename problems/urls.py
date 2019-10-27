from django.urls import path
from . import views

urlpatterns = [
    path('',views.problems, name = 'problems'),
    path('createproblem/', views.create, name = 'create'),
    path('<str:category>/', views.problemList, name = 'problem_list'),
    
]