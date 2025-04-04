import json
import os

from jsonschema import validate


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SCHEMAS_PATH = os.path.join(BASE_DIR, "schemas")


def load_json_schema(schema_name):
    schema_filename = f"{schema_name}.json"
    schema_path = os.path.join(SCHEMAS_PATH, schema_filename)
    with open(schema_path, "r", encoding = "utf-8") as file:
        return json.load(file)


def json_schema_validate(response, schema_name: str):
    json_schema = load_json_schema(schema_name = schema_name)
    response_body = response.json()
    validate(response_body, json_schema)
