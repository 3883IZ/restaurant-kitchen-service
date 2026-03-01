from django.contrib import admin
from django.urls import path, include
from kitchen.views import (
    DishListView,
    DishDetailView,
    CategoryListView,
    CategoryDetailView,
    register,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse

def health_check(request):
    return HttpResponse("Service is running")

urlpatterns = [
    path("admin/", admin.site.urls),

    # Health-check для Render
    path("health/", health_check, name="health_check"),

    # Список страв з пагінацією та пошуком
    path("", DishListView.as_view(), name="home"),
    path("dishes/", DishListView.as_view(), name="dish_list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish_detail"),

    # Категорії
    path("categories/", CategoryListView.as_view(), name="category_list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),

    # Авторизація
    path("accounts/logout/", LogoutView.as_view(next_page="home"), name="logout"),
    path("accounts/register/", register, name="register"),
    path("accounts/", include("django.contrib.auth.urls")),
]

# 🔹 Для демо: віддаємо медіа навіть у продакшн
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
