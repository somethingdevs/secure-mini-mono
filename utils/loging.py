import logging
import sqlite3


class log:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.console_handler = logging.StreamHandler()
        self.log_format = '%(asctime)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(self.log_format)
        self.console_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.console_handler)

    def log_info(self, message, inp=None):
        # print('in logger info with var ',inp)
        self.console_handler.setLevel(logging.INFO)
        self.logger.setLevel(logging.INFO)
        if (inp):
            self.logger.info(message, inp)
        else:
            self.logger.info(message)

    def log_debug(self, message, inp=None):
        self.console_handler.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.DEBUG)
        logging.Formatter(self.log_format)

        self.logger.addHandler(self.console_handler)
        if (inp):
            self.logger.debug(message, inp)
        else:
            self.logger.debug(message)

    def log_error(self, message, inp=None):
        self.console_handler.setLevel(logging.ERROR)
        self.logger.setLevel(logging.ERROR)
        logging.Formatter(self.log_format)
        if (inp):
            self.logger.error(message, inp)
        else:
            self.logger.error(message)
