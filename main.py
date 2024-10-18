import redis
from rq import Queue, Worker
from tasks import execute_after
from datetime import datetime, timedelta
from rq.decorators import job

REDIS_URL = "redis://localhost:6379/0"

r = redis.from_url(REDIS_URL)

# Create the default queue
queue = Queue(connection=r)

# Create the queue for high priority jobs
high_priority_q = Queue(connection=r , name="high")

# Create the queue for low priority jobs
low_priority_q = Queue(connection=r, name="low")

# Create a worker instance and bind it to the default queue
worker = Worker([queue, high_priority_q, low_priority_q], connection=r)

# Create many jobs at once
queue.enqueue_many([
    Queue.prepare_data(execute_after,[10], job_id="1"),
    Queue.prepare_data(execute_after,[10], job_id="2"),
    Queue.prepare_data(execute_after,[20], job_id="3"),
    Queue.prepare_data(execute_after,[30], job_id="4"),
    Queue.prepare_data(execute_after,[40], job_id="5"),
    Queue.prepare_data(execute_after,[50], job_id="6"),
])

# create a job to execute at a certain time
job_to_run = queue.enqueue_at(datetime(2024,10,19,20,6,0), execute_after,12, job_id="12")


# create a job to execute after a certain time
job_to_run2 = queue.enqueue_in(timedelta(seconds=6), execute_after, 12, job_id="13")

# create a job using Celery-like decorator
@job("default",connection=r)
def add(x,y):
    return x + y

# run a worker
worker.work()







