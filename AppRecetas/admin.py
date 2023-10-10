from django.contrib import admin

# Register your models here.
from AppRecetas.models import *

admin.site.register(RecetasMain)
admin.site.register(RecetasUsr)
admin.site.register(Cheff)
admin.site.register(Avatar)
