from django.contrib import admin
from .models import Regiao, Lider, Grupo
from  django.contrib.auth.models  import  Group  # new

admin.site.register(Regiao)
admin.site.register(Lider)
admin.site.register(Grupo)

#...
admin.site.unregister(Group)  # new
