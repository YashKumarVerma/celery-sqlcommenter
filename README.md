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
![a simple celery task that takes a while](./docs/images/aws-rds-session-query.png)

## More Questions?
Please open an issue or drop a message on my socials, will be happy to help.

[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yash-kumar-verma/)
[![X](https://img.shields.io/badge/X-%23000000.svg?style=for-the-badge&logo=X&logoColor=white)](https://x.com/yash_kr_verma)


## How to publish 
- poetry build
- poetry config pypi-token.pypi <your-pypi-token>
- poetry publish