
# unicode utc=8

from django.contrib import admin

# Register your models here.
from ahcoop.models import Historia
admin.site.register(Historia)

from ahcoop.models import Escritores
admin.site.register(Escritores)

from ahcoop.models import Participantes
admin.site.register(Participantes)

from ahcoop.models import Regras
admin.site.register(Regras)

from ahcoop.models import Partes
admin.site.register(Partes)
