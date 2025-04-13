from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app.pedidos.views import formulario_cliente, vista_exito

urlpatterns = [
    # 🌐 Rutas públicas del cliente
    path('', formulario_cliente, name='formulario_cliente'),
    path('formulario/', formulario_cliente, name='formulario_cliente'),
    path('exito/', vista_exito, name='exito'),

    # 🔐 Admin y autenticación JWT
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📦 APIs
    path('api/usuarios/', include('app.usuarios.urls')),
    path('api/pedidos/', include('app.pedidos.urls')),

    # 🌐 Vistas HTML para mesero, cocinero, etc.
    path('', include('app.pedidos.urls')),  # 👈 ESTA es la línea que faltaba
]

# 🧾 Archivos media (solo en modo desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
