import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

def setup_logger(name="snowflake_pipeline", log_file="app.log", level=logging.INFO):
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    full_path = log_dir / log_file

    formatter = logging.Formatter(
        "{asctime} - {levelname} - {message} ",
        style="{",
        datefmt="%Y-%m-%d - %H:%M"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        full_path,
        backupCount=3,
        maxBytes=1024*1024
    )
    file_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    if logger.hasHandlers:
        return logger
    
    logger.setLevel(level)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger