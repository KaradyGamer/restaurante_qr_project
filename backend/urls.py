from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from app.pedidos.views import formulario_cliente, menu_cliente

urlpatterns = [
    # 🌐 Vistas públicas del cliente (sin login)
    path('', formulario_cliente, name='formulario_cliente'),           # Página inicial
    path('formulario/', formulario_cliente, name='formulario_cliente'),  # Acceso directo al formulario
    path('menu/', menu_cliente, name='menu_cliente'),                  # Menú del cliente

    # 🔐 Admin y JWT
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 🔒 APIs protegidas y de cliente
    path('api/usuarios/', include('app.usuarios.urls')),
    path('api/pedidos/', include('app.pedidos.urls')),
]

# 🧾 Archivos multimedia (solo en desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
