import pytest
import json
import os

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com/"

@pytest.fixture(scope="session")
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "data", "endpoints_config.json")
    with open(config_path, "r") as f:
        return json.load(f)

@pytest.fixture(scope="function")
def load_payload(request):
    endpoint = request.param
    payload_path = os.path.join(os.path.dirname(__file__), "..", "data", "payloads", "posts_payloads.json")
    try:
        with open(payload_path, "r") as f:
            payloads = json.load(f)
            payload = payloads.get(endpoint, None)
            return (payload, endpoint)
    except (FileNotFoundError, KeyError):
        return (None, endpoint)
@pytest.fixture(scope="session")
def load_expectation():
    expectations_path = os.path.join(os.path.dirname(__file__), "..", "data", "expectations", "posts_expectations.json")
    with open(expectations_path, "r") as f:
        data = json.load(f)
        return data