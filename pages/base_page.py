import requests
from src.data import Urls


class BasePage:
    def __init__(self):
        self.base_url = Urls.BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def make_request(self, method, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(
            method=method, url=url, json=data, headers=headers
        )
        return response

    def get(self, endpoint, headers=None):
        return self.make_request("GET", endpoint, headers=headers)

    def post(self, endpoint, data=None, headers=None):
        return self.make_request("POST", endpoint, data=data, headers=headers)

    def delete(self, endpoint, data=None, headers=None):
        return self.make_request("DELETE", endpoint, data=data, headers=headers)
