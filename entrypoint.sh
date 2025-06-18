#!/usr/bin/env bash

# Exit immediately if any command exits with a non-zero status
set -e


# Step 1: Run database migrations
echo "Running database migrations..."
python manage.py makemigrations || { echo "Makemigrations failed"; exit 1; }
python manage.py migrate || { echo "Migration failed"; exit 1; }


# Step 2: Create superuser
echo "Creating superuser (if not exists)..."

python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists():
    User.objects.create_superuser(
        '${DJANGO_SUPERUSER_USERNAME}',
        '${DJANGO_SUPERUSER_EMAIL}',
        '${DJANGO_SUPERUSER_PASSWORD}'
    )
"

# Step 3: Start the Django server 
echo "Starting the server..."
python manage.py runserver 0.0.0.0:8000