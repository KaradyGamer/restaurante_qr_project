# ✅ app/pedidos/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'', views.PedidoViewSet)

urlpatterns = [
    # ───── Cliente ─────
    path('cliente/crear/', views.crear_pedido_cliente, name='crear_pedido_cliente'),
    path('formulario/', views.formulario_cliente, name='formulario_cliente'),
    path('menu/', views.menu_cliente, name='menu_cliente'),
    path('exito/', views.vista_exito, name='exito'),

    # ───── Cocinero ─────
    path('cocinero/login/', views.login_cocinero, name='login_cocinero'),
    path('panel-cocina/', views.panel_cocina, name='panel_cocina'),
    path('en-cocina/', views.PedidosEnCocinaAPIView.as_view(), name='en_cocina'),
    path('actualizar/<int:pedido_id>/', views.actualizar_estado_pedido, name='actualizar_estado_pedido'),

    # ───── Mesero ─────
    path('mesero/login/', views.login_mesero, name='login_mesero'),
    path('mesero/panel/', views.vista_para_meseros, name='panel_mesero'),
    path('mesero/', views.pedidos_por_mesa, name='pedidos_por_mesa'),

    # ───── ViewSet ─────
    path('', include(router.urls)),
]
