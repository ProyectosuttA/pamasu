from django.db import models
from django.contrib.auth.models import User

class Registro(models.Model):
    id_carta=models.CharField(max_length=40, primary_key=True, null=False)
    pedido = models.CharField(max_length=40)
    folio = models.CharField(max_length=40)
    origen = models.CharField(max_length=40)
    destino = models.CharField(max_length=40)
    maniobras = models.CharField(max_length=40)
    diesel = models.CharField(max_length=40)
    gastos = models.CharField(max_length=40)
    hora_reporte = models.DateTimeField()
    inicio_carga = models.DateTimeField()
    termino_carga = models.DateTimeField()
    inicio_ruta = models.DateTimeField()
    arribo_cliente = models.DateTimeField()
    inicio_descarga = models.DateTimeField()
    termino_descarga = models.DateTimeField()
    termino_viaje = models.DateTimeField()
    def __str__(self):
        return self.id_carta+' REGISTRO'  

class Comentarios(models.Model):
    carta=models.ForeignKey(Registro, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comentario=models.TextField()
    def __str__(self):
        return f'- Ralizado - {self.user.username} - A REGISTRO - {self.carta.id_carta}'
    
    
