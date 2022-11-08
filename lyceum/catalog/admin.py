from django.contrib import admin

from .models import Category, Galery, Item, Preview, Tag

admin.site.register(Category)
admin.site.register(Tag)


class GaleryInline(admin.StackedInline):
    model = Galery
    readonly_fields = ('image_tmb',)
    extra = 1


class ItemInline(admin.StackedInline):
    model = Item


@admin.register(Preview)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tmb')
    inlines = [
        ItemInline,
    ]


@admin.register(Galery)
class GaleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tmb', 'item_name')

    def item_name(self, obj):
        return obj.item.name
    item_name.short_description = 'товар'


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'image_tmb')
    list_editable = ('is_published',)
    list_display_links = ('name',)
    filter_horizontal = ('tags',)
    inlines = [
        GaleryInline,
    ]

    def image_tmb(self, obj):
        if obj.preview:
            return obj.preview.image_tmb()
        return 'Нет изображения'
    image_tmb.short_description = 'превью'
