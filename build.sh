#!/usr/bin/env bash
set -o errexit

# Встановлення залежностей
pip install -r requirements.txt

# Збір статичних файлів
python manage.py collectstatic --no-input

# Міграції
python manage.py migrate

# 🔹 Медіа не копіюємо — вони вже є у контейнері
echo "Media files will be served directly from /media/"
