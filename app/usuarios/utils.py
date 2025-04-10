from django.http import HttpResponseForbidden

def rol_requerido(rol_permitido):
    def decorador(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated or request.user.rol != rol_permitido:
                return HttpResponseForbidden("No tienes permiso para acceder a esta vista.")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorador
