from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PedidoViewSet,
    crear_pedido_cliente,
    formulario_cliente,
    menu_cliente,
)

# 🔐 Rutas para personal (con login)
router = DefaultRouter()
router.register(r'', PedidoViewSet)

# ✅ Rutas completas
urlpatterns = [
    # Rutas API
    path('cliente/', crear_pedido_cliente),   # 🔓 API pública para crear pedidos
    path('', include(router.urls)),           # 🔐 CRUD API para staff

    # Rutas HTML (cliente)
    path('formulario/', formulario_cliente, name='formulario_cliente'),
    path('menu/', menu_cliente, name='menu_cliente'),
]
