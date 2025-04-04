import pytest
import requests

from helpers.data import base_url
from helpers.validate import json_schema_validate


def test_successful_register():
    url = f'{base_url}/register'
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    payload = {
        'email': email,
        'password': password
    }

    response = requests.post(url, json = payload)
    print(response.json())
    assert response.status_code == 200
    json_schema_validate(response, schema_name = 'register')


@pytest.mark.parametrize("payload, expected_error", [
    ({"email": "eve.holt@reqres.in"}, "Missing password"),
    ({"password": "pistol"}, "Missing email or username")
])
def test_unsuccessful_register(payload, expected_error):
    url = f'{base_url}/register'

    response = requests.post(url, json = payload)
    response_body = response.json()
    assert response.status_code == 400
    assert response_body["error"] == expected_error
