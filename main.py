import logging

from fastapi import FastAPI, Request
from pythonjsonlogger import jsonlogger


def setup_logger(level: int = logging.INFO) -> logging.Logger:
    logger: logging.Logger = logging.getLogger(__name__)
    
    if logger.handlers:
        return logger
    
    logger.setLevel(level)
    handler: logging.StreamHandler = logging.StreamHandler()
    formatter: jsonlogger.jsonFormatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s %(filename)s %(lineno)d"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger


app: FastAPI = FastAPI()
logger: logging.Logger = setup_logger()


@app.get("/")
def root(request: Request) -> dict:
    """Root endpoint."""

    logger.info("hello world", extra={"endpoint": "/"})

    result: dict = {
        "message": "Hello, World!"
    }
    return result
