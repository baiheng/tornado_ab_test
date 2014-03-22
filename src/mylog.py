#!/usr/bin/pypy
# -*-coding:utf-8-*- 

import logging
import logging.config
import sys

class Log:
    def __init__(self):
        home_path = sys.path[0]
        logging.config.fileConfig("%s/../conf/logging.conf" % home_path)
        self.logger = logging.getLogger("root")
        self.stat_logger = logging.getLogger("stat")

    def init(self):
        logging.config.fileConfig("./conf/logging.conf")
        self.logger = logging.getLogger("root")
        return [logger, handler]

    def DEBUG(self, msg):
        self.logger.debug(msg)

    def INFO(self, msg):
        self.logger.info(msg)

    def WARN(self, msg):
        self.logger.warn(msg)

    def ERROR(self, msg):
        self.logger.error(msg)

    def STAT(self, msg):
        self.stat_logger.info(msg)
LOG = Log()

