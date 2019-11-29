#!/bin/bash

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn coin_notify.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 3
