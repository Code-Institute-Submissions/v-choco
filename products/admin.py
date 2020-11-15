from django.contrib import admin
from .models import Product, Category, ProductReview

# Models


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp',
        'product',
        'user',
        'rating',
    )

    ordering = ('timestamp',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
