from django.contrib import admin
from .models import Post, Comentario, Visualizacion, Like, Usuario

admin.site.register(Usuario)
admin.site.register(Post)
admin.site.register(Comentario)
admin.site.register(Visualizacion)
admin.site.register(Like)
