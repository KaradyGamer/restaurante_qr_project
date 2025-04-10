# Generated by Django 5.2 on 2025-04-10 01:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mesas', '__first__'),
        ('productos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('preparando', 'Preparando'), ('listo', 'Listo'), ('entregado', 'Entregado')], default='pendiente', max_length=20)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mesas.mesa')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='pedidos.pedido')),
            ],
        ),
    ]
