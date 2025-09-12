from pages.base_page import BasePage
from src.data import Urls, UserData


class CourierPage(BasePage):
    def __init__(self):
        super().__init__()
        self.courier_creation_endpoint = Urls.COURIER_CREATION_ENDPOINT
        self.courier_login_endpoint = Urls.COURIER_LOGIN_ENDPOINT

    def generate_courier_data_valid(self):
        return {
            "login": UserData.generate_random_string(),
            "password": str(UserData.generate_random_number()),
            "firstName": UserData.generate_first_name(),
        }

    def generate_courier_data_no_login(self):
        return {
            "password": str(UserData.generate_random_number()),
            "firstName": UserData.generate_first_name(),
        }

    def generate_courier_data_no_password(self):
        return {
            "login": UserData.generate_random_string(),
            "firstName": UserData.generate_random_string(),
        }

    def generate_courier_data_no_firstname(self):
        return {
            "login": UserData.generate_random_string(),
            "password": str(UserData.generate_random_number()),
        }

    def create_courier(self, courier_data):
        return self.post(self.courier_creation_endpoint, data=courier_data)

    def login_courier(self, courier_data):
        payload = {"login": courier_data["login"], "password": courier_data["password"]}
        return self.post(self.courier_login_endpoint, data=payload)

    def delete_courier(self, courier_id):
        endpoint = f"{self.courier_creation_endpoint}/{courier_id}"
        return self.make_request("DELETE", endpoint)
