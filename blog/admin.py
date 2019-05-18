from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)   	#Registro de publicaciones.
admin.site.register(Comment)	#Registro de comentarios.