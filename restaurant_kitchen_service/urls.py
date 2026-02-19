from django.contrib import admin
from django.urls import path, include
from kitchen.views import dish_list, CategoryListView, category_dishes, register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import user_passes_test

# доступ лише для staff
admin.site.login = user_passes_test(lambda u: u.is_staff)(admin.site.login)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dish_list, name='home'),
    path('dishes/', dish_list, name='dish_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/dishes/', category_dishes, name='category_dishes'),

    # Авторизація
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
