from django.db import migrations

def create_default_category(apps, schema_editor):
    Category = apps.get_model("kitchen", "Category")
    if not Category.objects.filter(pk=1).exists():
        Category.objects.create(id=1, name="Default")

class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),  # або остання твоя міграція
    ]

    operations = [
        migrations.RunPython(create_default_category),
    ]
