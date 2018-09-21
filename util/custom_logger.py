# Author : Shreyas Ugemuge


import logging
import logging.config
import logging.handlers
import config as LG


def intiateConnection(logger):
    logger.info("init")
    logger.debug("init")
    logger.error("init - not an error")


def custom_logger(logLevel=logging.DEBUG):
    """returns the custom logger"""

    logger = logging.getLogger('root')
    logger.setLevel(logLevel)

    if not logger.handlers:
        debug_handler = logging.handlers.SocketHandler(
            'localhost', LG.DEBUG_PORT)
        debug_filter = filterFactory(
            _levels=[logging.CRITICAL,
                     logging.DEBUG])
        debug_handler.addFilter(debug_filter)
        logger.addHandler(debug_handler)

        error_handler = logging.handlers.SocketHandler(
            'localhost', LG.ERROR_PORT)
        error_filter = filterFactory(
            _levels=[logging.ERROR, logging.CRITICAL,
                     logging.WARNING])
        error_handler.addFilter(error_filter)
        logger.addHandler(error_handler)

        info_handler = logging.handlers.SocketHandler(
            'localhost', LG.INFO_PORT)
        info_filter = filterFactory(
            _levels=[logging.INFO])
        info_handler.addFilter(info_filter)
        logger.addHandler(info_handler)
        intiateConnection(logger)
    return logger


class filterFactory(logging.Filter):
    """Creates a filter that logs only desired logs, not sure why this
    is not standard functionality"""

    def __init__(self, _levels=[logging.INFO, logging.ERROR,
                                logging.DEBUG, logging.WARNING,
                                logging.CRITICAL]):
        self.__levels = _levels
        pass

    def filter(self, record):
        return record.levelno in self.__levels