import pytest
import allure
from pages.courier_page import CourierPage


class TestCourierCreation:

    @allure.title("Проверка создания курьера с валидными данными")
    def test_create_courier_success(self, delete_courier_data):

        page, set_courier_id = delete_courier_data

        courier_data = page.generate_courier_data_valid()
        response = page.create_courier(courier_data)

        print("Login:", courier_data["login"])
        print("Password:", courier_data["password"])

        assert response.status_code == 201
        body = response.json()
        assert body.get("ok") is True

        login_response = page.login_courier(courier_data)
        courier_id = login_response.json().get("id")
        assert courier_id is not None

        set_courier_id(courier_id)

    @allure.title("Проверка создания курьера с пустым логином")
    def test_create_courier_empty_login(self):
        courier = CourierPage()

        courier_data = courier.generate_courier_data_no_login()
        response = courier.create_courier(courier_data)

        assert response.status_code == 400
        body = response.json()
        assert body.get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка создания курьера с пустым паролем")
    def test_create_courier_empty_password(self):
        courier = CourierPage()

        courier_data = courier.generate_courier_data_no_password()
        response = courier.create_courier(courier_data)

        assert response.status_code == 400
        body = response.json()
        assert body.get("message") == "Недостаточно данных для создания учетной записи"

    @allure.title("Проверка создания дубликата курьера")
    @allure.issue("Баг: Некорректное описание ошибки")
    def test_create_courier_duplicate(self, delete_courier_data):
        page, set_courier_id = delete_courier_data

        courier_data = page.generate_courier_data_valid()
        response = page.create_courier(courier_data)
        response = page.create_courier(courier_data)
        assert response.status_code == 409
        body = response.json()
        assert body.get("message") == "Этот логин уже используется"

        login_response = page.login_courier(courier_data)
        courier_id = login_response.json().get("id")
        assert courier_id is not None

        set_courier_id(courier_id)
