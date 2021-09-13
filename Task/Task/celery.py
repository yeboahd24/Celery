import os
from celery import Celery

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Task.settings')

app = Celery('Task')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
app.conf.broker_url = BASE_REDIS_URL

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
