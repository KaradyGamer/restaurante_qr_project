# app/pedidos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PedidoViewSet,
    crear_pedido_cliente,
    formulario_cliente,
    menu_cliente,
    PedidosEnCocinaAPIView,
    actualizar_estado_pedido,
    vista_exito,
    login_cocinero,
    panel_cocina
)

# CRUD API para cocineros (protegido por permiso EsCocinero)
router = DefaultRouter()
router.register(r'', PedidoViewSet)

urlpatterns = [
    # Cliente
    path('cliente/crear/', crear_pedido_cliente, name='crear_pedido_cliente'),
    path('formulario/', formulario_cliente, name='formulario_cliente'),
    path('menu/', menu_cliente, name='menu_cliente'),
    path('exito/', vista_exito, name='exito'),

    # Cocinero
    path('login-cocinero/', login_cocinero, name='login_cocinero'),
    path('panel-cocina/', panel_cocina, name='panel_cocina'),
    path('en-cocina/', PedidosEnCocinaAPIView.as_view(), name='en_cocina'),
    path('actualizar/<int:pedido_id>/', actualizar_estado_pedido, name='actualizar_estado_pedido'),

    # ViewSet API
    path('', include(router.urls)),
]
