import pytest
import allure
from pages.order_api import OrderApi
from src.data import SCOOTER_COLOR


class TestOrderCreation:

    @pytest.mark.parametrize("scooter_color", SCOOTER_COLOR)
    @allure.title("Проверка создания заказа")
    def test_create_order_success(self, scooter_color):
        order = OrderApi()

        order_data = order.generate_order_data_valid(scooter_color)
        print(order_data)
        response = order.create_order(order_data)

        assert response.status_code == 201
        body = response.json()
        track = body.get("track")
        assert track is not None
