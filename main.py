import os
from handler import load_vars


def main():
    yaml = load_vars.YamlHandler()
    variable_map = yaml.load_yaml('config/env_variables.yml')

    for k, v in variable_map.items():
        os.environ[k] = v


if __name__ == "__main__":
    main()
