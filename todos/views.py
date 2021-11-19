from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todo


class ListTodo(ListView):
	model = Todo
	template_name = 'index.html'
	context_object_name = 'todos'

class CreateTodo(CreateView):
	model = Todo
	fields = ['title']
	template_name = 'create_todo.html'


class UpdateTodo(UpdateView):
	model = Todo
	fields = ['title']
	template_name = 'update_todo.html'


class DeleteTodo(DeleteView):
	model = Todo
	template_name = 'delete_todo.html'
	success_url = reverse_lazy('list-todo')
