from django.contrib import admin

from .models import Category, Gallery, Item, Preview, Tag


class GalleryInline(admin.TabularInline):
    model = Gallery
    readonly_fields = ('image_tmb',)
    extra = 1


class PreviewInline(admin.TabularInline):
    model = Preview
    readonly_fields = ('image_tmb',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'is_published', 'weight')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('small_image_tmb', 'item_name')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'small_image_tmb',
        'name',
        'category_name',
        'is_published',
        'is_on_main'
    )
    list_editable = ('is_published', 'is_on_main')
    list_display_links = ('name',)
    filter_horizontal = ('tags',)
    fields = ('name', 'category', 'tags', 'text', 'is_published', 'is_on_main')
    inlines = [
        PreviewInline,
        GalleryInline,
    ]

    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = 'категория'

    def small_image_tmb(self, obj):
        if obj.preview:
            return obj.preview.small_image_tmb()
        return 'Нет изображения'
    small_image_tmb.short_description = 'превью'


@admin.register(Preview)
class PreviewAdmin(admin.ModelAdmin):
    list_display = ('small_image_tmb', 'item_name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'is_published')
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
