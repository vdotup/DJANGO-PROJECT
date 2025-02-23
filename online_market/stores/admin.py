from django.contrib import admin

from .models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'owner']


# Register your models here.
admin.site.register(Store, StoreAdmin)
