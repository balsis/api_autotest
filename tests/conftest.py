import pytest
import requests

from helpers import generate
from helpers.data import base_url


@pytest.fixture
def create_test_user():
    url = f'{base_url}/users'
    payload = {
        'name': generate.name,
        'job': generate.job
    }
    response = requests.post(url, json = payload)
    assert response.status_code == 201
    user = response.json()
    return user['name'], user['job'], user['id']