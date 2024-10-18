# Background Processing with RQ 

## What is RQ?

RQ is a Python library that allows users to queue jobs and process them in the background using workers. It is built on top of Redis. 

## Why use RQ?
- It is very simple to use. (can be a very good alternative to using Celery)
- It is ver simple to add to existing projects
- It is very capable of handling large volumes of tasks
- It has built in support for retrying failed tasks and monitoring task status.

## Installing RQ

```bash
pip install rq
```

You will also need to have Redis installed for these examples to work.

## Setting up RQ

```python
from rq import Queue
from redis import Redis

redis = Redis()

q = Queue(connection=redis)

```

## Create a function

```python
import time
from datetime import datetime

def some_slow_task(time_taken):
    print("################################")
    print(f"This task will run for {time_taken} seconds")
    start_time = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
    print(f"Started at {start_time}")
    time.sleep(time_taken)

    end_time = datetime.strftime(datetime.now(),"%Y-%m-%%d %H:%M:%S")
    print(f"Finished at {end_time}")
    print("Task finished")
    print("#################################")

```

## Enqueue a job

```python
from rq import Queue
from redis import Redis

redis = Redis()

q = Queue(connection=redis)

# a job
job = q.enqueue(some_slow_task,12)

print(job.id)
```

## Enqueue a job on a specific queue

```python
from rq import Queue
from redis import Redis

redis = Redis()

q = Queue(name="simple",connection=redis)

job = q.enqueue(some_slow_task, 13)
```

## Enqueuing multiple jobs

```python
from rq import Queue
from redis import Redis

redis = Redis()

q = Queue(connection=redis)

q.enqueue_many([
    Queue.prepare_data(some_slow_task, [12], job_id="1"),
    Queue.prepare_data(some_slow_task, [10], job_id="2"),
    Queue.prepare_data(some_slow_task, [8], job_id="3"),
])
```

## Run a worker

```bash
rq worker
```

## Creating a worker script
```python
from redis import Redis
from rq import Worker, Queue, Connection
from my_module import do_work

conn = Redis('localhost', 6379)
queue = Queue(connection=conn)
worker = Worker([queue], connection=redis)
worker.work()
```
## schedule jobs to run at a given time

```python
from rq import Queue
from redis import Redis
from datetime import datetime

redis = Redis()

q = Queue(connection=redis)

q.enqueue_at(datetime(2024,10,11),some_slow_task, 12, job_id="whatever")
```

## scehdule jobs to run after a certain amount of time
```python
from rq import Queue
from redis import Redis
from datetime import timdelta

redis = Redis()

q = Queue(connection=redis)

q.enqueue_in(timedelta(minutes=5),some_slow_task, 12, job_id="whatever")
```

## Monitoring Tasks with RQ Dashboard
```bash
pip install rq-dashboard


rq-dashboard --port 8000
```

## Celery style jobs
```python
from rq.decorators import job
from redis import Redis
from datetime import datetime

redis = Redis()


# create a job
@job('my_queue',connection=redis,timeout=5)
def add(x,y):
    return x + 
```
