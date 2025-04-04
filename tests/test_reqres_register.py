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

    assert response.status_code == 200
    json_schema_validate(response, schema_name = 'register')


def test_unsuccessful_register_without_password():
    url = f'{base_url}/register'
    email = 'eve.holt@reqres.in'

    payload = {
        'email': email,
    }

    response = requests.post(url, json = payload)
    response_body = response.json()
    assert response.status_code == 400
    assert response_body['error'] == "Missing password"
