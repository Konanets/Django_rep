import os
from celery.schedules import crontab
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')
app = Celery('configs')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_spam_every_minute':{
        'task':'core.services.email_service.spam',
        'schedule':crontab( )
    }
}