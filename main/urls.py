from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('problems/', views.problems, name = 'problems'),
    path('submissions/', views.submissions, name = 'submissions'),
    path('about/', views.about, name = 'about'),
]