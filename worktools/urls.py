from django.contrib import admin
from django.urls import path, include
from .views import  ListTool, DetailTool, DeleteTool, CreateTool, UpdateTool

app_name = 'worktools'

urlpatterns = [
    path('', ListTool, name='list'),
    path('<int:id>/', DetailTool, name='detail'),
    path('create/', CreateTool.as_view(), name='create'),
    path('update/<int:id>/', UpdateTool.as_view(), name='update'),
    path('delete/', DeleteTool, name='delete')
]
