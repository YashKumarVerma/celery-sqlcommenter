from .query_wrapper import QueryWrapper
from contextlib import ExitStack
from celery import Task
from django.db import connections


class BaseTask(Task):
    def __call__(self, *args, **kwargs):
        with ExitStack() as stack:
            for db_alias in connections:
                stack.enter_context(
                    connections[db_alias].execute_wrapper(QueryWrapper(self.name))
                )
            self.run(*args, **kwargs)
