from django.contrib import admin
from django.urls import path, include
from .views import CreateUser, ListUsers, UserDetail, UpdateUser, DeleteUser

app_name = 'accounts'
urlpatterns = [
    path('', ListUsers, name='list'),
    path('<int:id>/', UserDetail, name='detail'),
    path('create/', CreateUser.as_view(), name='create'),
    path('update/<int:id>/', UpdateUser.as_view(), name='update'),
    path('delete/', DeleteUser, name='delete')
]
