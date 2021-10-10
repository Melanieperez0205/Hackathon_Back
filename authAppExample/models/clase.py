from django.db import models
from .user  import User

class Clase(models.Model):
    id                = models.AutoField(primary_key=True)
    idusuario         = models.ForeignKey(User, related_name='Usuario_que_toma_la_clase', on_delete=models.CASCADE)
    temaclase         = models.CharField(max_length=100)
    descripcionclase  = models.CharField(max_length=100)