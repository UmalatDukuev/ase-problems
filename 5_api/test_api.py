import pytest
import requests
import unittest
class TestPetAPI:
    base_url = "https://petstore.swagger.io/v2/pet"
#создание pet и его ошибки
    @pytest.mark.create
    def test_create_pet(self):
        url = self.base_url
        headers = {"Content-Type": "application/json"}
        data = {
            "id": 1,
            "category": {
                "id": 1,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.post(url, json=data, headers=headers)
        assert response.status_code == 200
        assert response.json()["name"] == "doggie"
    @pytest.mark.create
    def test_create_pet_invalid_input(self):
        url = self.base_url
        response = requests.get(url)
        assert response.status_code == 405

# редактирование pet и его ошибки
    @pytest.mark.edit
    def test_update_pet(self):
        url = self.base_url
        headers = {"Content-Type": "application/json"}
        data = {
            "id": 1,
            "category": {
                "id": 2,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.put(url, json=data, headers=headers)
        assert response.status_code == 200
        assert response.json()["id"] == 1
        assert response.json()["name"] == "doggie"

    @pytest.mark.edit
    def test_update_pet_invalid_id(self):
        url = self.base_url
        data = {"id": -12, "name": "Fluffy5"}  # Invalid input
        response = requests.put(url, json=data)
        assert response.status_code == 200

#поиск pet по статусу и его ошибки
    @pytest.mark.find
    def test_find_petByStatus(self):
        url = self.base_url + "/findByStatus"
        params = {'status': 'available'}
        response = requests.get(url, params=params)
        assert response.status_code == 200
        for pet in response.json():
            assert pet['status'] == "available"
    @pytest.mark.find
    def test_find_petByStatus_Invalid_status_value(self):
        url = self.base_url + "/findByStatus"
        params = {'status': '1'}
        response = requests.get(url, params=params)
        print(response.json())
        # assert response.status_code == 200
        # for pet in response.json():
        #     assert pet['status'] == "available"

# поиск pet по айди и его ошибки
    @pytest.mark.find
    def test_find_petById(self):
        petid = 1
        url = self.base_url + f"/{petid}"
        response = requests.get(url)
        assert response.status_code == 200
        assert response.json()["id"] == 1

    @pytest.mark.find
    def test_find_petById_not_found(self):
        petid = 1021
        url = self.base_url + f"/{petid}"
        response = requests.get(url)
        print(response.json())
        assert response.status_code == 404
        assert response.json()["message"] == "Pet not found"

    @pytest.mark.find
    def test_find_petById_InvalidIdSupplied(self):
        petid = 1
        url = self.base_url + f"/{petid}"
        response = requests.get(url)
        assert response.status_code == 404
        #assert response.json()["message"] == "Invalid ID supplied"