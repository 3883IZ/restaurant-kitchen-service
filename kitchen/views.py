from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Category, Dish

# Функціональний view для всіх страв з пошуком і пагінацією
def dish_list(request):
    query = request.GET.get("q")
    dishes = Dish.objects.all()
    if query:
        dishes = dishes.filter(name__icontains=query)

    paginator = Paginator(dishes, 6)  # 6 страв на сторінку
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.prefetch_related("dishes").all()
    return render(
        request,
        "kitchen/dish_list.html",
        {"categories": categories, "page_obj": page_obj, "query": query},
    )

# Функціональний view для страв конкретної категорії з пошуком і пагінацією
def category_dishes(request, pk):
    category = get_object_or_404(Category.objects.prefetch_related("dishes"), pk=pk)
    query = request.GET.get("q")
    dishes = category.dishes.all()
    if query:
        dishes = dishes.filter(name__icontains=query)

    paginator = Paginator(dishes, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "kitchen/dish_list.html",
        {"categories": [category], "page_obj": page_obj, "query": query},
    )

# Клас‑based view для категорій
class CategoryListView(ListView):
    model = Category
    template_name = "kitchen/category_list.html"
    context_object_name = "categories"
