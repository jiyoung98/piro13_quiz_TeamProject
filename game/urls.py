from django.contrib import admin
from django.urls import path, include
from .views import *

app_name='game'

urlpatterns = [
    path('', quiz_home, name='quiz_home'),
    path('create/', create, name='create'),
    path('solve_list/', solve_list, name='solve_list'),
    path('solve/<int:pk>/', solve, name='solve'),
    path('ranking/<int:pk>',ranking, name='ranking'),

]