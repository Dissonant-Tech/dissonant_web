#!/bin/bash

# Give time for the DB to start
sleep 5

python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

echo "from django.contrib.auth.models import User;" \
     "User.objects.create_superuser('$ADMIN_USER', '$ADMIN_EMAIL', '$ADMIN_PASS')" \
     | python manage.py shell

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn dissonant_website.wsgi:application \
    --name splyttr \
    --bind 0.0.0.0:8050 \
    --workers 3 \
    --log-level=info \
    "$@"
