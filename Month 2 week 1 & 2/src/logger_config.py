import logging
from logging.handlers import RotatingFileHandler
import os

def logger_setup(name="ETL", log_file="app.log", level=logging.INFO):
    # Create folder for logs and connect log file destination
    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", log_file)

    # Set up design of logger
    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M"
    )

    # Set up std out logging to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Set up output to logging file with size and backup count
    file_handler = RotatingFileHandler(
        log_path, # Base file name for output
        maxBytes= 1024 * 10, # Max suze if log file in bytes
        backupCount=4 # Number of backup logs to keep before deleting
    )
    file_handler.setFormatter(formatter)

    # Define logger
    logger = logging.getLogger(name)
    if logger.hasHandlers(): # Prevent duplicates
        return logger
    
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.propagate = False # Prevents logging being passed to parents

    return logger