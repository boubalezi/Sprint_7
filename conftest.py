import pytest
from pages.courier_api import CourierApi


@pytest.fixture
def courier_creation_and_delete_page():
    page = CourierApi()

    courier_data = page.generate_courier_data_valid()
    create_response = page.create_courier(courier_data)
    assert create_response.status_code == 201

    login_response = page.login_courier(courier_data)
    assert login_response.status_code == 200
    courier_id = login_response.json().get("id")
    assert courier_id is not None

    yield page, courier_data, courier_id

    delete_response = page.delete_courier(courier_id)
    assert delete_response.status_code == 200


@pytest.fixture
def delete_courier_data():
    page = CourierApi()

    courier_id_holder = {"id": None}

    def set_courier_id(courier_id):
        courier_id_holder["id"] = courier_id

    yield page, set_courier_id

    if courier_id_holder["id"]:
        delete_response = page.delete_courier(courier_id_holder["id"])
        assert delete_response.status_code == 200
