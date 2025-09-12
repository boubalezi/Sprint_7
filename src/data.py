import random
import string
from faker import Faker

fake = Faker()


class Urls:
    BASE_URL = "https://qa-scooter.praktikum-services.ru"
    COURIER_CREATION_ENDPOINT = "/api/v1/courier"
    COURIER_LOGIN_ENDPOINT = "/api/v1/courier/login"
    ORDER_CREATION_ENDPOINT = "/api/v1/orders"
    GET_ORDER_LIST_ENDPOINT = "/api/v1/orders"


class UserData:
    LOGIN = "leopold"
    NONEXISTENT_LOGIN = "leopold100"
    PASSWORD = "1234"

    VALID_COURIER_DATA = {
        "login": "leopold",
        "password": "1234",
        "firstName": "leopold",
    }
    INVALID_COURIER_DATA_NO_LOGIN = {
        "login": "",
        "password": "1234",
        "firstName": "leopold",
    }
    INVALID_COURIER_DATA_NO_PASSWORD = {
        "login": "leopold",
        "password": "",
        "firstName": "leopold",
    }

    INVALID_COURIER_DATA_NO_FIRSTNAME = {
        "login": "leopold",
        "password": "1234",
        "firstName": "",
    }

    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_random_number():
        return str(random.randint(100000, 999999))

    @staticmethod
    def generate_first_name():
        return fake.first_name()

    @staticmethod
    def generate_last_name():
        return fake.last_name()

    @staticmethod
    def generate_random_phone_number():
        return "+7" + "".join(fake.random_choices(elements="0123456789", length=10))

    @staticmethod
    def generate_address():
        return fake.address().replace("\n", ", ")

    @staticmethod
    def generate_date():
        return fake.date()


SCOOTER_COLOR = ["BLACK", "GREY", ["BLACK", "GREY"], ""]
COMMENT = "I will be back"
