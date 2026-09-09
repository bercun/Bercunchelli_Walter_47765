from django.contrib import admin

# Register your models here.
from AppRecetas.models import *

admin.site.register(RecetasMain)
admin.site.register(RecetasUsr)
admin.site.register(Cheff)
admin.site.register(Avatar)


@admin.register(IngredientePrecio)
class IngredientePrecioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "unidad_base", "precio_estimado", "moneda", "updated_at")
    search_fields = ("nombre",)
    list_filter = ("unidad_base", "moneda")


class PasoInlineMain(admin.TabularInline):
    model = PasoMain
    extra = 1


class PasoInlineUsr(admin.TabularInline):
    model = PasoUsr
    extra = 1
