from django.contrib import admin
from ciem.apps.data.models import Entry
from ciem.apps.account.models import datosAntropometricos

admin.site.register(Entry)
admin.site.register(datosAntropometricos)