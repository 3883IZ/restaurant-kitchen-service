from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Dish, Category
from .forms import CustomUserCreationForm


class DishListView(ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"
    context_object_name = "dishes"
    paginate_by = 3
    ordering = ["name"]  # 🔹 додано сортування для стабільної пагінації

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
        # Використовуємо related_name="dishes"
        context["dishes"] = self.object.dishes.all()
        return context


# 🔹 Кастомна реєстрація з автоматичним логіном
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматичний логін
            return redirect("home")  # редірект на головну
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})
