import logging

def getLogger(__name__):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(levelname)s][%(asctime)s][%(module)s:%(funcName)s:%(lineno)d] %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger