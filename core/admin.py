from django.contrib import admin
from . import models


@admin.register(models.Tag)
class Tag(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )


@admin.register(models.Item)
class Item(admin.ModelAdmin):
    list_display = ("name", "done")
    search_fields = ("name", )
