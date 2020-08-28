import configparser
from common.dir_config import *


class ReadConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(global_config_dir)
        switch = self.config.get("switch", "on")
        if switch:
            self.config.read(online_config_dir)
        else:
            self.config.read(test_config_dir)

    def get(self, section, option):
        return self.config.get(section, option)


config = ReadConfig()
