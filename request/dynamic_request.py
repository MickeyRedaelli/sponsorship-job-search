import requests


class Request:

    def __init__(self):
        pass

    @staticmethod
    def dynamic_request(**kwargs: dict) -> str | dict:
        method = kwargs.get('method', 'get').lower()
        endpoint = kwargs.get('endpoint')
        structure = kwargs.get('structure', 'json')

        if not endpoint:
            raise ValueError("Endpoint must be provided")
        if not method:
            raise ValueError(f"Invalid method: {method}")

        kwargs.pop('method')
        kwargs.pop('endpoint')
        kwargs.pop('structure')

        method = getattr(requests, method)
        response = method(endpoint, **kwargs)
        return getattr(response, structure)
