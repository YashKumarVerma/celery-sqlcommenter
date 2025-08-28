from contextlib import ExitStack
from celery import Task
from django.db import connections

from .query_wrapper import QueryWrapper


class BaseTask(Task):
    def __call__(self, *args, **kwargs):
        task_name = self.name or "celery-task"
        with ExitStack() as stack:
            for db_alias in connections:
                stack.enter_context(
                    connections[db_alias].execute_wrapper(QueryWrapper(task_name))
                )
            return self.run(*args, **kwargs)
