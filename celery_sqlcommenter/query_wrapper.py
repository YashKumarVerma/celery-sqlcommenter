from .utils import add_sql_comment


class QueryWrapper:
    def __init__(self, task_name: str):
        self.task_name = task_name

    def __call__(self, execute, sql, params, many, context):
        # Initialize a dictionary to hold additional comment parameters
        additional_comments = {
            "celery_task": self.task_name
        }
        sql = add_sql_comment(sql, **additional_comments)
        return execute(sql, params, many, context)
