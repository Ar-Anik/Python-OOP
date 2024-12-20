""" Monkey patching is often used in unit tests to mock or replace parts of the code with test-specific logic. """

import requests

original_get = requests.get

class APIClient:
    def fetch_data(self, url):
        response = requests.get(url)
        print("Response Object : ", response)
        return response.json()

def mocked_get(url):
    """ Mocked version of requests.get that retrieves and modifies the actual response. """

    real_response = original_get(url)

    """ Return a mock response object that modifies the real response data """
    return MockResponse(real_response)

class MockResponse:
    def __init__(self, real_response):
        self.real_response = real_response

    def json(self):
        real_data = self.real_response.json()

        modified_data = [
            {
                **item,
                "modified": True,
                "summary": item['body'].split("\n")[0]
            }
            for item in real_data
        ]

        return modified_data

requests.get = mocked_get

client = APIClient()
data = client.fetch_data("https://jsonplaceholder.typicode.com/posts/?_limit=5")

print("Data : ", data)


