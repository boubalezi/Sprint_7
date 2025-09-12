import allure
from src.data import UserData
from pages.courier_page import CourierPage


class TestCourierLogin:

    @allure.title("Проверка логина курьера с валидными данными")
    def test_courier_login_valid_data(self):

        courier = CourierPage()
        courier_valid_data = {"login": UserData.LOGIN, "password": UserData.PASSWORD}

        login_response = courier.login_courier(courier_valid_data)
        assert login_response.status_code == 200
        body = login_response.json()
        courier_id = login_response.json().get("id")
        assert body.get("id") == courier_id

    @allure.title("Проверка логина курьера с пустым логином")
    def test_courier_login_with_empty_login(self):
        courier = CourierPage()
        courier_data_only_password = UserData.INVALID_COURIER_DATA_NO_LOGIN

        login_response = courier.login_courier(courier_data_only_password)
        assert login_response.status_code == 400
        body = login_response.json()
        assert body.get("message") == "Недостаточно данных для входа"

    @allure.title("Проверка логина курьера с пустым паролем")
    def test_courier_login_with_empty_password(self):
        courier = CourierPage()
        courier_data_only_login = UserData.INVALID_COURIER_DATA_NO_PASSWORD

        login_response = courier.login_courier(courier_data_only_login)
        assert login_response.status_code == 400
        body = login_response.json()
        assert body.get("message") == "Недостаточно данных для входа"

    @allure.title("Проверка логина несуществующего курьера")
    def test_nonexistent_courier_login(self):
        courier = CourierPage()
        nonexistent_courier_data = {
            "login": UserData.NONEXISTENT_LOGIN,
            "password": "password",
        }

        login_response = courier.login_courier(nonexistent_courier_data)
        assert login_response.status_code == 404
        body = login_response.json()
        assert body.get("message") == "Учетная запись не найдена"

    @allure.title("Проверка логина курьера с невалидным логином")
    def test_courier_login_with_invalid_login(self, courier_creation_and_delete_page):
        page, courier_data, _ = courier_creation_and_delete_page
        courier_data_invalid_login = {
            "login": UserData.LOGIN,
            "password": (courier_data["password"]),
        }

        login_response = page.login_courier(courier_data_invalid_login)
        assert login_response.status_code == 404
        body = login_response.json()
        assert body.get("message") == "Учетная запись не найдена"

    @allure.title("Проверка логина курьера с невалидным паролем")
    def test_courier_login_with_invalid_password(
        self, courier_creation_and_delete_page
    ):
        page, courier_data, _ = courier_creation_and_delete_page
        courier_data_invalid_password = {
            "login": (courier_data["login"]),
            "password": UserData.PASSWORD,
        }

        login_response = page.login_courier(courier_data_invalid_password)
        assert login_response.status_code == 404
        body = login_response.json()
        assert body.get("message") == "Учетная запись не найдена"
