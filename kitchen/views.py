from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout
from .models import Category, Dish
from .forms import CustomUserCreationForm


# 🔹 Головна сторінка доступна всім
def dish_list(request):
    query = request.GET.get("q")
    dishes = Dish.objects.all()
    if query:
        dishes = dishes.filter(name__icontains=query)

    paginator = Paginator(dishes, 6)  # 6 страв на сторінку
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    return render(
        request,
        "kitchen/dish_list.html",
        {"categories": categories, "page_obj": page_obj, "query": query},
    )


# 🔹 Категорії теж доступні всім
def category_dishes(request, pk):
    category = get_object_or_404(Category, pk=pk)
    query = request.GET.get("q")
    dishes = category.dishes.all()
    if query:
        dishes = dishes.filter(name__icontains=query)

    paginator = Paginator(dishes, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "kitchen/category_dishes.html",
        {"category": category, "page_obj": page_obj, "query": query},
    )


class CategoryListView(ListView):
    model = Category
    template_name = "kitchen/category_list.html"
    context_object_name = "categories"


# 🔹 Деталі страви
class DishDetailView(DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    context_object_name = "dish"


# 🔹 Реєстрація користувачів
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматичний логін після реєстрації
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


# 🔹 Кастомний Logout
def logout_view(request):
    logout(request)
    return redirect("home")
