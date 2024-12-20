import pytest
import requests
import json
from jsonschema import validate
from jsonpath_ng import parse
from tests.BaseClass import BaseClass


class TestingAPI:
    BASE_URL = "https://fakestoreapi.com/"
    headers = {"Content-Type": "application/json"}
    token = "asndjasdasjdn"
    headers1 = {"Authorization": f"Bearer {token}", **headers}

    JSON_Schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Generated schema for Root",
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "number"
                },
                "title": {
                    "type": "string"
                },
                "price": {
                    "type": "number"
                },
                "description": {
                    "type": "string"
                },
                "category": {
                    "type": "string"
                },
                "image": {
                    "type": "string"
                },
                "rating": {
                    "type": "object",
                    "properties": {
                        "rate": {
                            "type": "number"
                        },
                        "count": {
                            "type": "number"
                        }
                    },
                    "required": [
                        "rate",
                        "count"
                    ]
                }
            },
            "required": [
                "id",
                "title",
                "price",
                "description",
                "category",
                "image",
                "rating"
            ]
        }
    }

    def test_getRequest(self):
        logger = BaseClass.getLogger()
        response = requests.get(f"{self.BASE_URL}/products", headers=self.headers)
        assert response.status_code == 200, "incorrect status code"
        assert response.elapsed.total_seconds() < 5000, "Response time is greater than 5 seconds"
        logger.info(response.text)
        logger.info(response.headers.get("Content-Type"))
        logger.info("Response JSON:", json.dumps(response.json(), indent=4))

        self.json_schema_validator(response.json(), self.JSON_Schema)
        self.json_path_validation(response.json(), "$[5].[price]", 168)
        # self.json_path_validation(response.json(), "$[*].title", "168")

    def test_postMethod(self,setup_logger_and_object_creation):
        logger = BaseClass.getLogger()
        logger.info("sangar")
        Payload = {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        serialisedPayload = serialisedData(Payload)
        response = requests.post(f"{self.BASE_URL}/products", headers=headers1, data=serialisedPayload)
        logger.info(response.status_code)
        logger.info(response.text)


    def serialisedData(self, response):
        return json.dumps(response.json())

    def json_schema_validator(self, response, json_schema):
        try:
            validate(instance=response, schema=json_schema)
            logger.info(f"Json schema Matches with expected")
        except Exception as e:
            logger.info(f"JSon schema not matches:{e}")

    def json_path_validation(self, response, json_path, expectedValue):
        try:
            json_path_runner = parse(json_path)
            match = [match.value for match in json_path_runner.find(response)]
            assert match == [expectedValue], f"expected {expectedValue} but got{match}"
        except Exception as e:
            logger.info(f"Exception occured:json path validation failed {e}")
