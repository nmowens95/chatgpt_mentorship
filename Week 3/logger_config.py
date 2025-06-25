import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name="summarizer", log_file="app.log", level=logging.INFO):
    # Check if log directory exists
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", log_file)

    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # File Handler with Rotation
    file_handler = RotatingFileHandler(
        log_path,
        maxBytes=1024 * 10,
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    # Set up the logger
    logger = logging.getLogger(name)
    if logger.hasHandlers(): # Prevent duplicates
        return logger
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.propagate = False # Prevent double logging if using root logger

    return logger