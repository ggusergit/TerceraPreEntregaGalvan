from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Veterinario)
admin.site.register(Mascota)
admin.site.register(Dueño)
admin.site.register(Turno)