from django.urls import path

from .views import (
    ListTodo,
    CreateTodo,
    UpdateTodo,
    DeleteTodo,
)


urlpatterns = [
    path('', ListTodo.as_view(), name='list-todo'),
    path('create/', CreateTodo.as_view(), name='create-todo'),
    path('update/<int:pk>', UpdateTodo.as_view(), name='update-todo'),
    path('delete/<int:pk>', DeleteTodo.as_view(), name='delete-todo'),
]
