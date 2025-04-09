from rest_framework import serializers
from .models import Pedido, DetallePedido
from app.productos.models import Producto

class DetallePedidoSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)

    class Meta:
        model = DetallePedido
        fields = ['id', 'producto', 'producto_nombre', 'cantidad', 'subtotal']
        read_only_fields = ['id', 'producto_nombre', 'subtotal']

class PedidoSerializer(serializers.ModelSerializer):
    detalles = DetallePedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ['id', 'mesa', 'fecha', 'estado', 'total', 'detalles']
        read_only_fields = ['id', 'fecha', 'estado', 'total']

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        pedido = Pedido.objects.create(**validated_data)

        total = 0
        for detalle in detalles_data:
            producto = detalle['producto']
            cantidad = detalle['cantidad']
            subtotal = producto.precio * cantidad
            total += subtotal

            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=cantidad,
                subtotal=subtotal
            )

        pedido.total = total
        pedido.save()
        return pedido
