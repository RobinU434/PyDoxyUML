import logging


def set_log_level(log_level: str):
    """sets log level

    Args:
        log_level (str): _description_
    """
    log_levels = {
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG,
        "notset": logging.NOTSET,
    }
    logging.basicConfig(level=log_levels[log_level])
