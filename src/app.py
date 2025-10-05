from fastapi import FastAPI
import logging
import sys
from loguru import logger
from asgi_correlation_id.context import correlation_id
from asgi_correlation_id import CorrelationIdMiddleware


def configure_logging() -> None:
    """
    Configure application logging with correlation ID support.

    Returns:
        None
    """

    def correlation_id_filter(record):
        """
        Log filter function that adds correlation ID to log records.

        Parameters:
            record (dict): The log record dictionary to be modified

        Returns:
            bool: Always returns True to indicate the record should be processed
        """
        record["correlation_id"] = correlation_id.get() or "no-request"
        return True

    logger.remove()
    fmt = "{level}: \t  {time} {name}:{line} [{correlation_id}] - {message}"
    logger.add(
        sys.stderr, format=fmt, level=logging.DEBUG, filter=correlation_id_filter
    )


app = FastAPI(
    title="Minha Palavra API",
    description="API for work with contracts",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
    on_startup=[configure_logging],
)

app.add_middleware(CorrelationIdMiddleware)


@app.get("/")
def healthy():
    return {"status": "healthy"}
