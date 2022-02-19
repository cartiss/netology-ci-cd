from django.contrib import admin

# Register your models here.
from logistic.models import Stock, Product, StockProduct


class ProductStockInline(admin.TabularInline):
    model = StockProduct


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductStockInline,
    ]


class StockAdmin(admin.ModelAdmin):
    inlines = [
        ProductStockInline,
    ]
    exclude = ('products',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Stock, StockAdmin)
