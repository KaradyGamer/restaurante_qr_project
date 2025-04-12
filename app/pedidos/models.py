from django.db import models
from app.productos.models import Producto
from app.mesas.models import Mesa
from django.utils import timezone

# 🆕 Constantes fuera de la clase para orden
FORMA_PAGO_CHOICES = [
    ('efectivo', 'Efectivo'),
    ('qr', 'QR'),
    ('tarjeta', 'Tarjeta'),
]

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('preparando', 'Preparando'),
            ('listo', 'Listo'),
            ('entregado', 'Entregado'),
        ],
        default='pendiente'
    )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # ✅ Ahora más claro visualmente
    forma_pago = models.CharField(max_length=10, choices=FORMA_PAGO_CHOICES, default='efectivo')

    def __str__(self):
        return f"Pedido #{self.id} - Mesa {self.mesa.numero}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
