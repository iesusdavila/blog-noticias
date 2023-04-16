from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comentario, Visualizacion, Like
from .forms import PostFormulario

class VistaListaPosts(ListView):
    model = Post

class VistaDetallePost(DetailView):
    model = Post    

class VistaCreaPost(CreateView):
    form_class = PostFormulario
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "Crear"
        return context
    

class VistaActualizaPost(UpdateView):
    form_class = PostFormulario
    model = Post
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "Actualizar"
        return context

class VistaBorraPosts(DeleteView):
    model = Post
    success_url = '/'
  