#!/usr/bin/env bash
set -o errexit

# Встановлення залежностей
pip install -r requirements.txt

# Збір статичних файлів
python manage.py collectstatic --no-input

# Міграції
python manage.py migrate

# Копіювання медіа у контейнер (щоб Render бачив фото)
if [ -d "media" ]; then
  echo "Copying media files..."
  cp -r media $PWD/
else
  echo "No media directory found, skipping."
fi
