from django.contrib import admin
from rating.models import Rating

from .models import Category, Gallery, Item, MainImage, Tag


class GalleryInline(admin.TabularInline):
    model = Gallery
    readonly_fields = ('image_tmb',)
    extra = 1


class RatingInline(admin.TabularInline):
    model = Rating


class MainImageInline(admin.TabularInline):
    model = MainImage
    readonly_fields = ('image_tmb',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'is_published', 'weight')
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)


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
    fields = (
        'name',
        'category',
        'tags',
        'text',
        'is_published',
        'is_on_main',
        # 'rating',
    )
    inlines = [
        MainImageInline,
        GalleryInline,
        RatingInline,
    ]

    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = 'категория'

    def small_image_tmb(self, obj):
        if obj.mainimage:
            return obj.mainimage.small_image_tmb()
        return 'Нет изображения'
    small_image_tmb.short_description = 'главное изображение'


@admin.register(MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = ('small_image_tmb', 'item_name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'is_published')
    list_display = ('name', 'is_published')
    list_editable = ('is_published',)
