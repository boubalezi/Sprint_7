from pages.base_api import BaseApi
from src.data import Urls, UserData, COMMENT


class OrderApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.order_creation_endpoint = Urls.ORDER_CREATION_ENDPOINT
        self.get_order_list_endpoint = Urls.GET_ORDER_LIST_ENDPOINT

    def generate_order_data_valid(self, scooter_color):
        return {
            "firstName": UserData.generate_first_name(),
            "lastName": UserData.generate_last_name(),
            "address": UserData.generate_address(),
            "metroStation": UserData.generate_random_number(),
            "phone": UserData.generate_random_phone_number(),
            "rentTime": UserData.generate_random_number(),
            "deliveryDate": UserData.generate_date(),
            "comment": COMMENT,
            "color": [scooter_color],
        }

    def create_order(self, order_data):
        return self.post(self.order_creation_endpoint, data=order_data)

    def get_order_list(self):
        return self.get(self.get_order_list_endpoint)
