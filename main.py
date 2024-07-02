import os
from handler import load_vars
from request import dynamic_request


def main():
    # set env variables
    yaml = load_vars.YamlHandler()
    variable_map = yaml.load_yaml('config/env_variables.yml')
    for k, v in variable_map.items():
        os.environ[k] = v

    # Get govuk html to find the sponsor list
    request = dynamic_request.Request()

    govuk_html = request.dynamic_request(method='GET',
                           endpoint=os.getenv('uk-gov-register-of-sponsors'),
                           structure='text')


if __name__ == "__main__":
    main()
