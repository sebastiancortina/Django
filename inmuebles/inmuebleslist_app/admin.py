from django.contrib import admin
from inmuebleslist_app.models import Edificacion, Empresa, Comentario #referencia del modelo

# Register your models here.
admin.site.register(Edificacion)
admin.site.register(Empresa)
admin.site.register(Comentario)