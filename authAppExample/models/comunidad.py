from django.db import models
from .post import Article

class Comunidad(models.Model):
    id              = models.AutoField(primary_key=True)
    tipoComunidad   = models.CharField(max_length=25)
    register_date   = models.DateTimeField(auto_now_add=True, blank=True)
    descripcion     = models.CharField(max_length=100)
    id_post         = models.ForeignKey(Article, related_name='nombre_post', on_delete=models.CASCADE, default = None)