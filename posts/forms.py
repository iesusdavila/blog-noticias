from django import forms 
from .models import Post, Comentario

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('contenido',)         