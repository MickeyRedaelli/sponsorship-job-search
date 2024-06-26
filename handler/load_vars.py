import yaml


class YamlHandler:

    def __init__(self):
        pass

    @staticmethod
    def load_yaml(var_file: str) -> dict:
        with open(var_file) as f:
            return yaml.safe_load(f)
