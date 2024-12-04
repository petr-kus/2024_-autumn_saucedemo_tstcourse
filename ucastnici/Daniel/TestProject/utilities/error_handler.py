from selenium.common.exceptions import NoSuchElementException, TimeoutException

def handle_error(error, logger):
    """Handles errors and logs them."""
    logger.error(f"Error encountered: {str(error)}")
    if isinstance(error, NoSuchElementException):
        logger.error("Element was not found.")
    elif isinstance(error, TimeoutException):
        logger.error("Action timed out.")
    else:
        logger.error("An unexpected error occurred.")