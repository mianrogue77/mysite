from django.db import models

# Create your models here.

# Modelo que define la estructura para el objeto 'Elemento'
class Elemento(models.Model):
    nombre = models.CharField(max_length = 100)
    habilitado = models.BooleanField()

    def __str__(self):
        return self.nombre

# Modelo que define la estructura para el objeto 'Efecto'
class Efecto(models.Model):
    element_one = models.ForeignKey(Elemento, on_delete = models.CASCADE, related_name = 'principal')
    key_word = models.CharField(max_length = 100)
    element_two = models.ForeignKey(Elemento, on_delete = models.CASCADE, related_name = 'versus')

    def __str__(self):
        return self.key_word

