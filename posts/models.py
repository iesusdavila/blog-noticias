from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.shortcuts import reverse
from django.utils.text import slugify

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
    slug = models.SlugField(unique=True, max_length=150, blank=True, editable=False)
    
    # String cuando se llama directamente a la clase
    def __str__(self):
        return self.titulo
    
    # Colocar como slug al titulo separado por guiones
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
            # Verificar si el slug ya existe, si es así, agregar un número al final
            counter = 1
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.titulo)}-{counter}"
                counter += 1
        super().save(*args, **kwargs)
    
    # Llamar al URL absoluto
    def get_absolute_url(self):
        return reverse("detalle-post", kwargs={'slug': self.slug})
    
    # URL cuando se da like a un post
    def get_like_url(self):
        return reverse("like", kwargs={'slug': self.slug})
    
    # Numero de comentarios
    @property
    def get_comentario_count(self):
        return self.comentario_set.all().count()
    
    # Listar todos los comentarios 
    @property
    def comentarios(self):
        return self.comentario_set.all()
    
    # Numero de visualizaciones
    @property
    def get_visualizacion_count(self):
        return self.visualizacion_set.all().count()
    
    # Fecha de la ultima vez visto el post
    @property
    def get_last_view_post(self):
        return self.visualizacion_set.last().fec_visual
    
    # Numero de likes
    @property
    def get_like_count(self):
        return  self.like_set.all().count()
    
      
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
    fec_visual = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username        

class Like(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    fec_like = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username 