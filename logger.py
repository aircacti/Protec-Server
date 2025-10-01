import logging

def setup_logging():
    logger = logging.getLogger("protec")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")

    # Console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File
    file_handler = logging.FileHandler("protec.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
