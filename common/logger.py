import logging
from common.dir_config import *


def get_logger(name):
    mylogger = logging.getLogger(name)
    mylogger.setLevel("DEBUG")
    fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d]"
    formatter = logging.Formatter(fmt=fmt)

    console_handler = logging.StreamHandler()
    console_handler.setLevel("DEBUG")
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(logs_dir)
    file_handler.setLevel("DEBUG")
    file_handler.setFormatter(formatter)
    mylogger.addHandler(file_handler)

    return mylogger