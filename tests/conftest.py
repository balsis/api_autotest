import pytest
import requests

from helpers import generate
from helpers.data import base_url


@pytest.fixture(scope = "function")
def create_test_user():
    url = f'{base_url}/users'
    payload = {
        'name': generate.name,
        'job': generate.job
    }
    response = requests.post(url, json = payload)
    assert response.status_code == 201
    user = response.json()
    name, job, user_id = user['name'], user['job'], user['id']
    return name, job, user_id


@pytest.fixture(scope = "function")
def create_and_delete_test_user():
    url = f'{base_url}/users'
    payload = {
        'name': generate.name,
        'job': generate.job
    }
    response = requests.post(url, json = payload)
    assert response.status_code == 201
    user = response.json()
    name, job, user_id = user['name'], user['job'], user['id']
    yield name, job, user_id
    url = f'{base_url}/users/{id}'
    response = requests.delete(url)
    assert response.status_code == 204
