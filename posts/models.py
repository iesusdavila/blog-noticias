from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.shortcuts import reverse

class Usuario(AbstractUser):
    # AbstractUser se encarga de username, mail y contraseña
    pass

    def __str__(self):
        return self.username
    

class Post(models.Model):
    titulo = models.CharField(max_length=75)
    contenido = models.TextField()
    # portada = models.ImageField()
    fec_publicacion = models.DateTimeField(auto_now_add=True)
    fec_actualizacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    slug = models.SlugField()

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("detalle-post", kwargs={'slug': self.slug})
    

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fec_cmt = models.DateTimeField(auto_now_add=True)
    contenido = models.TextField()

    def __str__(self):
        return self.usuario.username

class Visualizacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fec_cmt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username        

class Like(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fec_like = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username 