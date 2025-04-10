from rest_framework.permissions import BasePermission

# Clase base que compara el rol
class EsRol(BasePermission):
    rol = None  # Este valor lo definirá cada subclase

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.rol == self.rol

# Subclases específicas por cada rol
class EsCocinero(EsRol):
    rol = 'cocinero'

class EsMesero(EsRol):
    rol = 'mesero'

class EsGerente(EsRol):
    rol = 'gerente'

class EsAdministrador(EsRol):
    rol = 'admin'
