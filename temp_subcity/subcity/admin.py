from django.contrib import admin
from subcity.models import Show, Episode

class ShowAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Show, ShowAdmin)
admin.site.register(Episode)