# celery-sqlcommenter
Attach SQL comments to correlate celery tasks with SQL statements.


This helps in easily correlating slow performance with async tasks and giving insights into backend database performance. In short it provides some observability into the state of your client-side applications and their impact on the database’s server-side.

## When to use?
You're using [celery](https://docs.celeryq.dev/en/stable/) with django, and want to trace the origin of database queries.


## Does it replace / overlap [sqlcommenter](https://google.github.io/sqlcommenter/#frameworks)
No. I've been using sqlcommenter in production and it lacked the ability to annotate queries that were run in non-http context. Meaning all queries that originated from async flows were untagged. 

This package fills that gap.

## How to use

In a simple celery setup, just passing the `BaseTask` when declaring a celery object will do the job.
```py
# if not using a base class, pass directly where you declare celery config
from celery_sqlcommenter import BaseTask
app = Celery("my-awsome-application", task_cls=BaseTask)

```


If you already have a custom `BaseTask` with specific functionality, replace the original `celery.Task` with `celery_sqlcommenter.BaseTask`
```py
# old configuration
from celery import Task
class MyBaseTask(Task):

    # custom methods you've implemented
    def on_failure(self, exc, task_id, args, kwargs):
        pass


# simply replace Task with BaseTask provided by the package
from celery_sqlcommenter import BaseTask


# notice Task changed to BaseTask
class MyBaseTask(BaseTask):

    # custom methods you've implemented
    def on_failure(self, exc, task_id, args, kwargs):
        pass

```
_Internally BaseTask inherits `celery.Task` so all functionality stays intact_


## How to install
Install the package from pypi
```
# vanilla
pip install celery-sqlcommenter

# poetry 
poetry add celery-sqlcommenter
```

## How does it look live?
![a simple celery task that takes a while](https://private-user-images.githubusercontent.com/14032427/393391701-f024f48f-6e68-4830-ba68-5c85381bc639.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzM1MTY2MTksIm5iZiI6MTczMzUxNjMxOSwicGF0aCI6Ii8xNDAzMjQyNy8zOTMzOTE3MDEtZjAyNGY0OGYtNmU2OC00ODMwLWJhNjgtNWM4NTM4MWJjNjM5LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEyMDYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMjA2VDIwMTgzOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWVhNWE5ODE5YzZmYTY4ZDAwMTE4MjU5ZjU1YTc0ZTBkODZlYWFiNjkyOGIwMzYzMDQ0NTcwMzk3ZDRlZjE3NzImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.-tHzhAV9Uciq-TBtqbCIvFlqXAZ-2oJNc94cmWPOHe8)

## More Questions?
Please open an issue or drop a message on my socials, will be happy to help.

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yash-kumar-verma/)
[![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://x.com/yash_kr_verma)