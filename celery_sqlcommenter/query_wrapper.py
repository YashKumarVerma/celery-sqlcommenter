from .utils import add_sql_comment
from prometheus_client import Counter


CELERY_SQL_COMMENTER_METRIC = Counter(
    name="celery_sql_commenter_metric",
    documentation="queries initiated via celery tasks",
    labelnames=[
        "task_name"
    ]
)


class QueryWrapper:
    def __init__(self, task_name: str):
        self.task_name = task_name

    def __call__(self, execute, sql, params, many, context):
        # Initialize a dictionary to hold additional comment parameters
        additional_comments = {"celery_task": self.task_name}
        CELERY_SQL_COMMENTER_METRIC.labels(task_name=self.task_name).inc()
        sql = add_sql_comment(sql, **additional_comments)
        return execute(sql, params, many, context)
