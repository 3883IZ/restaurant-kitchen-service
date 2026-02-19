from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Category

# Функціональний view для всіх страв
def dish_list(request):
    categories = Category.objects.prefetch_related("dishes").all()
    return render(request, "kitchen/dish_list.html", {"categories": categories})

# Функціональний view для страв конкретної категорії
def category_dishes(request, pk):
    category = get_object_or_404(Category.objects.prefetch_related("dishes"), pk=pk)
    return render(request, "kitchen/dish_list.html", {"categories": [category]})

# Клас‑based view для категорій
class CategoryListView(ListView):
    model = Category
    template_name = "kitchen/category_list.html"
    context_object_name = "categories"
