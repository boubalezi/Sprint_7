import pytest
import allure
from pages.order_page import OrderPage


class TestOrderList:

    @allure.title("Проверка получения списка заказов без указания id курьера")
    def test_get_order_list_withot_courier_id(self):
        order = OrderPage()

        response = order.get_order_list()

        assert response.status_code == 200
        body = response.json()
        assert "orders" in body
        orders_list = body["orders"]
        assert isinstance(orders_list, list)
        assert len(orders_list) > 0

        first_order = orders_list[0]
        expected_keys = [
            "id",
            "courierId",
            "firstName",
            "lastName",
            "address",
            "metroStation",
            "phone",
            "rentTime",
            "deliveryDate",
            "track",
            "color",
            "comment",
            "createdAt",
            "updatedAt",
            "status",
        ]
        for key in expected_keys:
            assert key in first_order
