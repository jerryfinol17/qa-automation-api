import pytest
import requests
from allure import step
import os
endpoints = ["users_get", "users_post", "users_put", "users_delete"]




@pytest.mark.parametrize("load_payload", endpoints, indirect=True)
def test_crud_posts(base_url, load_config, load_payload, load_expectation):
    payload, endpoint = load_payload
    headers = {"x-api-key": load_config.get("api_key", "reqres-free-v1")}
    config = load_config["endpoints"][endpoint]
    expected = load_expectation[endpoint]
    url = base_url + config["path"]
    params = config.get("params", {})

    with step(f"Execute {config['method']} request to {url}"):
        if config["method"] == "GET":
            response = requests.get(url, params=params)
        elif config["method"] == "POST":
            response = requests.post(url, json=payload, headers=headers)
        elif config["method"] == "PUT":
            response = requests.put(url, json=payload, headers=headers)
        elif config["method"] == "DELETE":
            response = requests.delete(url, headers=headers)
        response.raise_for_status()
    with step(f"Validate response for {endpoint}"):
        assert response.status_code == expected["status_code"]
        if expected["response_type"] == "none":
            assert response.text in ["", "{}"]
        else:
            data = response.json()
            if isinstance(data, dict) and "data" in data:
                data = data["data"]

            if expected["response_type"] == "none":
                assert response.text in ["", "{}"]
            else:
                if expected["response_type"] == "list":
                    assert isinstance(data, list) and len(data) > 0
                    sample_item = data[0]
                    assert all(key in sample_item for key in expected["required_keys"])
                elif expected["response_type"] == "dict":
                    assert isinstance(data, dict)
                    assert all(key in data for key in expected["required_keys"])


def test_users_get_with_page_filter(base_url, load_expectation):
    url = base_url + "/users"
    params = {"page": 2}
    expected = load_expectation["users_get"]
    with step("Execute GET /users with page=2 filter"):
        response = requests.get(url, params=params)
        response.raise_for_status()
    with step("Validate paginated response"):
        json_data = response.json()
        assert response.status_code == expected["status_code"]
        assert json_data["page"] == 2
        assert isinstance(json_data["data"], list) and len(json_data["data"]) == 6
        for item in json_data["data"]:
            assert all(key in item for key in expected["required_keys"])