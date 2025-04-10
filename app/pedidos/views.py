from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from django.utils import timezone

from .models import Pedido, DetallePedido
from .serializers import PedidoSerializer
from app.mesas.models import Mesa
from app.productos.models import Producto

from app.usuarios.utils import rol_requerido
from app.usuarios.permisos import EsCocinero  # ✅ CAMBIO AQUÍ


# 🔐 ViewSet solo accesible por cocineros
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all().order_by('-fecha')
    serializer_class = PedidoSerializer
    permission_classes = [EsCocinero]  # ✅ CORRECTO


# 🔐 Vista protegida para meseros (HTML)
@rol_requerido('mesero')
def vista_para_meseros(request):
    return render(request, 'mesero_panel.html')


# 🌐 Vista HTML para formulario del cliente
def formulario_cliente(request):
    productos_seleccionados = {}
    for key, value in request.GET.items():
        if key.startswith("producto_") and int(value) > 0:
            productos_seleccionados[key] = int(value)

    return render(request, 'cliente/formulario.html', {
        'productos_seleccionados': productos_seleccionados
    })


# 🌐 Vista HTML para menú del cliente
def menu_cliente(request):
    return render(request, 'cliente/menu.html')


# 🔓 Vista pública para crear pedidos desde el cliente
@api_view(['POST'])
@permission_classes([AllowAny])
def crear_pedido_cliente(request):
    try:
        mesa_id = request.data.get('mesa')
        detalles = request.data.get('detalles')

        if not mesa_id or not detalles:
            return Response({'error': 'Datos incompletos.'}, status=status.HTTP_400_BAD_REQUEST)

        mesa = Mesa.objects.get(id=mesa_id)
        pedido = Pedido.objects.create(mesa=mesa, fecha=timezone.now())

        total = 0
        for item in detalles:
            producto_id = item.get('producto')
            cantidad = item.get('cantidad', 1)
            producto = Producto.objects.get(id=producto_id)
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

        return Response({'mensaje': 'Pedido creado exitosamente', 'pedido_id': pedido.id}, status=status.HTTP_201_CREATED)

    except Mesa.DoesNotExist:
        return Response({'error': 'Mesa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    except Producto.DoesNotExist:
        return Response({'error': 'Producto no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# 🍽️ Vista API exclusiva para cocineros
class PedidosEnCocinaAPIView(APIView):
    permission_classes = [EsCocinero]  # ✅ CORRECTO

    def get(self, request):
        pedidos = Pedido.objects.all().order_by('-fecha')  # Podés agregar filtro por estado
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
