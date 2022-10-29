from django.contrib import admin

from .models import Item, Tag, Category


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('name',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Category, CategoryAdmin)
