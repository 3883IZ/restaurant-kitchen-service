from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Dish, Category


class DishListView(ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    context_object_name = "dishes"   # список страв
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q", "")
        return context


class DishDetailView(DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"
    context_object_name = "dish"


class CategoryListView(ListView):
    model = Category
    template_name = "kitchen/category_list.html"
    context_object_name = "categories"


class CategoryDetailView(DetailView):
    model = Category
    template_name = "kitchen/category_detail.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # додаємо список страв цієї категорії
        context["dishes"] = self.object.dish_set.all()
        return context


# 🔹 Стандартна реєстрація
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # після реєстрації перенаправляємо на login
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})
