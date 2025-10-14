from django.db import models
from variables.models import Variable

class Measurement(models.Model):
    variable = models.ForeignKey(Variable, on_delete=models.CASCADE, default=None)
    producto = models.CharField(max_length=100)
    color = models.CharField(null=True, blank=True, default=None)
    talla = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s %s %s' % (self.producto, self.color, self.talla, self.ubicacion)