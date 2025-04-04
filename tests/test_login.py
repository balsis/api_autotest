import requests

from helpers.data import base_url
from helpers.validate import json_schema_validate


def test_successful_login():
    url = f'{base_url}/login'
    email = 'eve.holt@reqres.in'
    password = 'cityslicka'

    payload = {
        'email': email,
        'password': password
    }

    response = requests.post(url, json = payload)

    assert response.status_code == 200
    json_schema_validate(response, schema_name = 'login')


def test_unsuccessful_login_without_password():
    url = f'{base_url}/login'
    email = 'epeter@klaven'

    payload = {
        'email': email,
    }

    response = requests.post(url, json = payload)
    response_body = response.json()
    assert response.status_code == 400
    assert response_body['error'] == "Missing password"
