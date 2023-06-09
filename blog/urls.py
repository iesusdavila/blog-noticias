from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    VistaListaPosts,
    VistaPostsPublicados,
    VistaDetallePost,
    VistaCreaPost,
    VistaActualizaPost,
    VistaBorraPosts,
    like
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', VistaListaPosts.as_view(), name='lista-posts'),
    path('publicaciones/', VistaPostsPublicados.as_view(), name='post-publicados'),
    path('crear/', VistaCreaPost.as_view(), name='crea-post'),
    path('<slug:slug>/', VistaDetallePost.as_view(), name='detalle-post'),
    path('<slug>/actualizar-post/', VistaActualizaPost.as_view(), name='actualiza-post'),
    path('<slug>/borrar-post/', VistaBorraPosts.as_view(), name='borra-post'),
    path('like/<slug>/', like, name='like'),
    path("__reload__/", include("django_browser_reload.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
