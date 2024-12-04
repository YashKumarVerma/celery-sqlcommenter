from .utils import add_sql_comment
import logging

logger = logging.getLogger(__name__)


class QueryWrapper:
    def __init__(self, task_name: str):
        self.task_name = task_name

    def __call__(self, execute, sql, params, many, context):
        # Initialize a dictionary to hold additional comment parameters
        additional_comments = {}

        # Attempt to retrieve the Celery task name if running within a Celery task
        if self.task_name:
            logger.debug("celery task detected: %s", self.task_name)
            print("celery task detected: " + self.task_name)
            try:
                additional_comments["celery_task"] = self.task_name
            except Exception as e:
                logger.debug(f"Unable to retrieve Celery task name: {e}")
        else:
            logger.debug("celery task not detected!")

        sql = add_sql_comment(sql, **additional_comments)
        logger.debug(">> final sql: %s", sql)
        return execute(sql, params, many, context)
