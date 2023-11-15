import pytest
import requests
import unittest

class TestPetAPI:
    base_url = "https://petstore.swagger.io/v2/pet"

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

    @pytest.mark.find
    def test_find_pet(self):
        url = self.base_url + "/findByStatus"
        params = {'status': 'available'}
        response = requests.get(url, params=params)
        assert response.status_code == 200
        for pet in response.json():
            assert pet['status'] == "available"