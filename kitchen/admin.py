from django.contrib import admin
from django.utils.html import format_html
from .models import Dish, Category


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "short_description", "image_preview")
    search_fields = ("name", "category__name", "description")
    list_filter = ("category",)
    ordering = ("name",)

    def short_description(self, obj):
        # показує перші 50 символів опису
        return (obj.description[:50] + "...") if obj.description else "-"
    short_description.short_description = "Description"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Image"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "image_preview")
    search_fields = ("name",)
    ordering = ("name",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:50px;"/>', obj.image.url)
        return "-"
    image_preview.short_description = "Image"
