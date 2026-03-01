from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    # Для демо можна залишити ImageField, якщо категорії мають власні фото
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        default="No description available"
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        Category,
        related_name="dishes",
        on_delete=models.CASCADE,
        null=False,
        default=1  # ID категорії "Default" (створи її в адмінці)
    )
    # 🔹 Заміна ImageField на CharField для роботи зі статикою
    # Тут зберігається шлях типу 'img/dishes/spaghetti.jpg'
    image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
