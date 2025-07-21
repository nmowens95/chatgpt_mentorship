import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def logger_setup(name="Medallion", log_file="app.logs", level=logging.INFO):
    output_dir = Path("logs")
    output_dir.mkdir(parents=True, exist_ok=True)
    full_path = output_dir/log_file

    formatter = logging.Formatter(
        "{asctime} - {level} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M"
    )

    # Create handlers
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        full_path,
        maxBytes=1024*10,
        backupCount=3
    )
    file_handler.setFormatter(formatter)

    # Create logger and add handlers
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger
    
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.propagate = False

    return logger