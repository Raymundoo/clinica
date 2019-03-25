from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Cita(models.Model):
	fecha_cita = models.DateField(db_index=True)
	hora_cita = models.TimeField(default=datetime.time(10, 10 ), verbose_name="Hora Facturacion")
	observacion = models.TextField(max_length=200, blank=True)
	created = models.DateTimeField(auto_now_add=True, editable=False)
	usuario = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="usuario_cita", null=True, blank=True)
	def __unicode__(self):
		return u'{0}'.format(self.id)

