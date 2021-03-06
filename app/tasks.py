from app.celery import celery
from celery.schedules import crontab
from celery.task import periodic_task


@celery.task()
def add_together(a, b):
    return a + b


@periodic_task(
    run_every=(crontab(hour='*/1', minute=0)),
    name="grab_adapter.tasks.status_update",
    ignore_result=True
)
def status_update():
    pass
