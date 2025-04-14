from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app.pedidos.views import formulario_cliente, vista_exito

urlpatterns = [
    # 🌐 Rutas públicas del cliente (landing page + formulario + exito)
    path('', formulario_cliente, name='formulario_cliente'),
    path('formulario/', formulario_cliente, name='formulario_cliente'),
    path('exito/', vista_exito, name='exito'),

    # 🔐 Admin y JWT
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📦 APIs del proyecto
    path('api/usuarios/', include('app.usuarios.urls')),
    path('api/pedidos/', include('app.pedidos.urls')),

    # 🌐 Vistas HTML (mesero, cocinero, etc.) → protegidas por permisos
    path('', include('app.pedidos.urls')),  # ← solo si contiene rutas fuera de /api/
]

# 🖼️ Media (solo en desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
