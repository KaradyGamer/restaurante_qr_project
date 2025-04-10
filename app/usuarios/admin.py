from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'rol', 'is_staff', 'is_superuser']

    # Campos visibles al editar un usuario
    fieldsets = UserAdmin.fieldsets + (
        ('Rol del usuario', {'fields': ('rol',)}),
    )

    # Campos visibles al crear un nuevo usuario
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rol del usuario', {'fields': ('rol',)}),
    )

admin.site.register(Usuario, UsuarioAdmin)
