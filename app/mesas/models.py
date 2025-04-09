import qrcode
import os
from io import BytesIO
from django.core.files import File
from django.db import models
from django.conf import settings

class Mesa(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('disponible', 'Disponible'),
            ('ocupada', 'Ocupada'),
            ('reservada', 'Reservada'),
        ],
        default='disponible'
    )
    qr_image = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return f"Mesa {self.numero}"

    def save(self, *args, **kwargs):
        url_qr = f"http://127.0.0.1:8000/menu/mesa/{self.id}/"  # Puedes cambiar la URL según el frontend real
        qr = qrcode.make(url_qr)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        file_name = f"mesa-{self.numero}-qr.png"
        self.qr_image.save(file_name, File(buffer), save=False)
        super().save(*args, **kwargs)
