from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Count
from .models import Post, Comentario, Visualizacion, Like, Usuario
from .forms import PostFormulario, ComentarioFormulario

class VistaListaPosts(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        # Enlistar los Posts con mas comentarios
        queryset = queryset.annotate(num_comentarios=Count('comentario')).order_by('-num_comentarios')[:6]
        return queryset
    
class VistaPostsPublicados(ListView):
    model = Post
    template_name = 'posts/posts_publicados.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Ordenar de acuerdo al numero de comentarios
        queryset = queryset.annotate(num_comentarios=Count('comentario')).order_by('-num_comentarios')
        return queryset

class VistaDetallePost(DetailView):
    model = Post

    def post(self, *args, **kwargs):
        form = ComentarioFormulario(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comentario = form.instance
            comentario.usuario = self.request.user
            comentario.post = post
            comentario.save()
            return redirect('detalle-post', slug=post.slug)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ComentarioFormulario
        return context

    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        Visualizacion.objects.get_or_create(usuario=self.request.user, post=object)
        return object

class VistaCreaPost(CreateView):
    form_class = PostFormulario
    model = Post
    success_url = '/'
    template_name = 'posts/post_create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "Crear"
        context['autores'] = Usuario.objects.all()
        context['autor_seleccionado'] = self.request.GET.get('autor')
        return context
    
class VistaActualizaPost(UpdateView):
    form_class = PostFormulario
    model = Post
    success_url = '/'
    template_name = 'posts/post_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["view_type"] = "Actualizar"
        context['autores'] = Usuario.objects.all()
        context['autor_seleccionado'] = self.request.GET.get('autor')
        return context

class VistaBorraPosts(DeleteView):
    model = Post
    success_url = '/'

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(usuario=request.user , post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detalle-post', slug=slug)
    Like.objects.create(usuario=request.user , post=post)
    return redirect('detalle-post', slug=slug)
  