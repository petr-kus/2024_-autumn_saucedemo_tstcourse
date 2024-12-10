import logging

def get_logger(name, log_file="test.log"):
    """Sets up a logger."""
    logger = logging.getLogger(name)
    if not logger.hasHandlers():

        # StreamHandler pro výstup na konzoli
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        # FileHandler pro uložení logů do souboru
        file_handler = logging.FileHandler(log_file, mode='w')
        file_handler.setLevel(logging.DEBUG)
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_formatter)
        filemode="w"
        logger.addHandler(file_handler)

    return logger