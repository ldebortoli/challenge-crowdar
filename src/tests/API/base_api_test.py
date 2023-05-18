import requests


class DefaultAPITesting:
    base_url = "https://www.mercadolibre.com.ar"
    default_headers = {
        #"Content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
    }


class APIResponse:

    def __init__(self, status_code, body):
        self.status_code = status_code
        self.body = body


class BaseAPITest:

    def send_request(self, method, path, headers={}, payload={}, entity_schema=None):
        url = f"{DefaultAPITesting.base_url}/{path}"
        headers.update(DefaultAPITesting.default_headers)

        if payload:
            response = requests.request(method, url, headers=headers, json=payload)
        else:
            response = requests.request(method, url, headers=headers)

        response_object = response.json()

        if entity_schema:
            response_object = entity_schema.load(response_object)

        return APIResponse(response.status_code, response_object)
