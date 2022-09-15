from django.db import models
from django.urls import reverse
from stores.models import Store


LABEL = (
    ('Usado', 'Usado'),
    ('Nuevo', 'Nuevo'),
    ('Oferta', 'Oferta'),
    ('Especial', 'Especial')
)
TYPE = (
    ('Cachucha', 'Cachucha'),
    ('Camiseta', 'Camiseta')

)

class Others(models.Model):
    label = models.CharField(max_length=50, blank=True, null=True, default='Nuevo', choices=LABEL)
    clotesType = models.CharField(max_length=50, blank=True, null=True, default='Nuevo', choices=TYPE)
    name = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    discount = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    cost = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    foto1 = models.ImageField(default='img/products/default.png', upload_to='img/products')
    foto2 = models.ImageField(upload_to='img/products', blank=True, null=True)
    foto3 = models.ImageField(upload_to='img/products', blank=True, null=True)
    
    def __str__(self):
        return self.name


# Nombre
# Marca
# precio
# descuento
# talla
# color
# material
# origen
# color
# descripcion 
# storage
# genero
# dimensiones
# envio
# disponivilidad
# madein
