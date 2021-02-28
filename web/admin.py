from django.contrib import admin

from .models import Item, ItemImage


class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 4


@admin.register(Item)
class ImageAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline, ]

@admin.register(ItemImage)
class ItemImageAdmin(admin.ModelAdmin):
    pass
