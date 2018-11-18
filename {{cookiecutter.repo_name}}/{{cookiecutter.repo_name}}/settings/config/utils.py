import os
from decouple import config
import yaml

__author__ = 'zpyoung'

CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    def __init__(self, yaml_file):
        self._file = os.path.join(CONFIG_DIR, yaml_file)
        if '.yaml' not in self._file:
            self._file = f'{self._file}.yaml'
        self.cget(self._file)

    def cget(self, yaml_file):
        _env = config("ENVIRONMENT", default="BASE").lower()
        with open(yaml_file) as file:
            y = yaml.load(file)
        for k, v in y['base'].items():
            setattr(self, k, v)
        if _env in y and _env != 'base':
            for k, v in y[_env].items():
                setattr(self, k, v)