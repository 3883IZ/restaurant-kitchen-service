from django.contrib import admin
from django.urls import path
from kitchen.views import dish_list, CategoryListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dish_list, name='home'),       # головна сторінка
    path('dishes/', dish_list, name='dish_list'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
