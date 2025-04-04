import requests

from helpers.data import base_url
from helpers.validate import json_schema_validate


def test_list_users():
    url = f'{base_url}/users'
    params = {"page": 1}
    response = requests.get(url, params = params)
    assert response.status_code == 200
    json_schema_validate(response = response, schema_name = "list_users")


def test_single_user():
    user_id = "2"
    url = f'{base_url}/users/{user_id}'
    response = requests.get(url)
    print(response.text)
    assert response.status_code == 200
    json_schema_validate(response = response, schema_name = "single_user")


def test_single_user_not_found():
    user_id = "23"
    url = f'{base_url}/users/{user_id}'
    response = requests.get(url)
    assert response.status_code == 404
    assert response.json() == {}


def test_create_user():
    url = f'{base_url}/users'
    name_in_request = 'John Doe'
    job_in_request = 'Worker'

    payload = {
        'name': name_in_request,
        'job': job_in_request
    }

    response = requests.post(url, json = payload)
    assert response.status_code == 201
    json_schema_validate(response, schema_name = 'create')
    name_in_response = response.json()["name"]
    job_in_response = response.json()["job"]
    assert name_in_request == name_in_response
    assert job_in_request == job_in_response


def test_update_user(create_and_delete_test_user):
    name, job, id = create_and_delete_test_user
    url = f'{base_url}/users/{id}'

    payload = {
        'name': name,
        'job': job
    }

    response = requests.patch(url, json = payload)
    assert response.status_code == 200
    json_schema_validate(response, schema_name = 'update')


def test_delete_user(create_test_user):
    name, job, id = create_test_user
    url = f'{base_url}/users/{id}'
    response = requests.delete(url)
    assert response.status_code == 204
    assert response.text is ""
