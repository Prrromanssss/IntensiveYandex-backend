from django.contrib import admin

from .models import Item, Tag, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tags',)


admin.site.register(Tag)
admin.site.register(Category)
