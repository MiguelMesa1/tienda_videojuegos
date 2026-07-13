from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
# AbstractUser: Tiene todos los campos y métodos que ya tiene un usuario de Django(username, password,etc)
class Usuario(AbstractUser):
    email = models.EmailField(unique=True) # cambiando comportamiento por defecto que tiene este campo en Django

    # Evitar conflictos de reverse accessors
    # Relación Muchos a muchos: cada usuario pertenece a varios grupos y cada grupo puede tener varios usuarios
    groups = models.ManyToManyField( #Relación de muchos a muchos con el modelo group
        Group,
        related_name='usuarios_set',  # aquí cambia el related_name
        blank=True,
        help_text='Grupos a los que pertenece este usuario.',
        verbose_name='groups',
    )
    # permisos individuales al usuario.
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_user_set',  # aquí cambia el related_name
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username