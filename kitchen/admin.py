from django.contrib import admin
from .models import Dish, Category


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "short_description")
    search_fields = ("name", "category__name", "description")
    list_filter = ("category",)
    ordering = ("name",)

    def short_description(self, obj):
        # показує перші 50 символів опису
        return (obj.description[:50] + "...") if obj.description else "-"
    short_description.short_description = "Description"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
