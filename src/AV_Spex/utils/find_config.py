import os
import sys
from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class ConfigPath:
    def __init__(self):
        self.config_dir = resource_path("config")
        self.config_yml = os.path.join(self.config_dir, 'config.yaml')
        self.reload()

    def reload(self):
        with open(self.config_yml) as f:
            self.config_dict = yaml.load(f)


class CommandConfig:
    def __init__(self):
        self.config_dir = resource_path("config")
        self.command_yml = os.path.join(self.config_dir, 'command_config.yaml')
        self.reload()

    def reload(self):
        with open(self.command_yml) as f:
            self.command_dict = yaml.load(f)


# Create an instance of the ConfigPath class
config_path = ConfigPath()

# Create an instance of the CommandConfig class
command_config = CommandConfig()
