#!/bin/bash

alembic upgrade head

case "$ENV" in
"DEV")
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ;;
"PROD")
    gunicorn app.main:app --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --workers "$GUNICORN_WORKERS" --timeout "$GUNICORN_TIMEOUT"
    ;;
*)
    echo "there is no environment"
    exit 1
    ;;
esac
