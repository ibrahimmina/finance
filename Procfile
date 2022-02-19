web: flask db upgrade; flask translate compile; gunicorn finance:app
worker: rq worker finance-tasks
