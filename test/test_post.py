import pytest
import requests
from allure import step

endpoints = ["posts_get", "posts_post", "posts_put", "posts_delete"]

@pytest.mark.parametrize("load_payload", endpoints, indirect=True)
def test_crud_posts(base_url, load_config, load_payload, load_expectation):
    payload, endpoint = load_payload
    config = load_config["endpoints"][endpoint]
    expected = load_expectation[endpoint]
    url = base_url + config["path"]
    params = config.get("params", {})

    with step(f"Execute {config['method']} request to {url}"):
        if config["method"] == "GET":
            response = requests.get(url, params=params)
        elif config["method"] == "POST":
            response = requests.post(url, json=payload)
        elif config["method"] == "PUT":
            response = requests.put(url, json=payload)
        elif config["method"] == "DELETE":
            response = requests.delete(url)
        response.raise_for_status()
    with step(f"Validate response for {endpoint}"):
        assert response.status_code == expected["status_code"]
        if expected["response_type"] == "none":
            assert response.text in ["", "{}"]
        else:
            data = response.json()
            if expected["response_type"] == "list":
                assert isinstance(data, list) and len(data) > 0
                sample_item = data[0]
                assert all(key in sample_item for key in expected["required_keys"])
            elif expected["response_type"] == "dict":
                assert isinstance(data, dict)
                assert all(key in data for key in expected["required_keys"])
                if payload:
                    assert data["title"] == payload["title"]
                    if "body" in payload:
                        assert data["body"] == payload["body"]


def test_posts_get_with_user_filter(base_url, load_expectation):
    url = base_url + "/posts"
    params = {"userId": 1}
    expected = load_expectation["posts_get"]
    with step("Execute GET /posts with userId=1 filter"):
        response = requests.get(url, params=params)
        response.raise_for_status()
    with step("Validate filtered response"):
        data = response.json()
        assert response.status_code == expected["status_code"]
        assert isinstance(data, list) and len(data) == 10
        for item in data:
            assert item["userId"] == 1
            assert all(key in item for key in expected["required_keys"])