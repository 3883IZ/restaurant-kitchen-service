from django.shortcuts import render
from .models import Category

def dish_list(request):
    categories = Category.objects.prefetch_related("dishes").all()
    return render(request, "kitchen/dish_list.html", {"categories": categories})
