import logging


def initLogger(logger_name, logger_file):
    # create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # File Handler
    file_handler = logging.FileHandler(logger_file)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # File Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    # 给logger添加handler
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def get_default_logger():
    logger = initLogger('test_logger', 'logs/test_logger.log')
    return logger
