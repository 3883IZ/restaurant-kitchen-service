from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(
        default="No description available"  # дефолт для всіх рядків
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        Category,
        related_name="dishes",
        on_delete=models.CASCADE,
        null=False,
        default=1  # ID категорії "Default" (створи її в адмінці)
    )
    image = models.ImageField(upload_to="dishes/", blank=True, null=True)

    def __str__(self):
        return self.name
