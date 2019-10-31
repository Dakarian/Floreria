from django.contrib import admin

from .models import Flores

class FlorAdmin(admin.ModelAdmin):
    list_display = ['name','descripcion','stock','valor']
    search_fields = ['name']
    list_per_page = 10
    


admin.site.register(Flores,FlorAdmin)
