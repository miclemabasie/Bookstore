from django.contrib import admin
from .models import Product, ProductImage, ProductTag
from django.utils.html import format_html

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'slug', 'active', 'in_stock', 'date_updated']
    list_filter = ['active', 'in_stock', 'date_updated']
    list_editable = ['in_stock']
    search_fields = ['name']
    autocomplete_fields = ('tags',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_tag', 'product_name']
    readonly_fields = ('thumbnail',)
    search_fields = ('product_name',)

    def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="%s"/>' % obj.thumbnail.url
            )
        return "-"
        thumbnail_tag.short_description = "Thumbnail"
    def product_name(self, obj):
        return obj.product.name
admin.site.register(ProductImage, ProductImageAdmin)


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'active']
    list_filter = ['active']
    list_editable = ('active',)
    search_fields = ('name',)
    prepopulated_fields = {'slug':  ('name',)}


admin.site.register(ProductTag, ProductTagAdmin)