import pytest

def test_check_base_and_config(base_url, load_config, load_expectation):
    assert base_url == "https://reqres.in/api"
    config = load_config["endpoints"]
    assert "users_get" in config
    exp = load_expectation
    assert exp["users_get"]["status_code"] == 200

@pytest.mark.parametrize("load_payload", ["users_post"], indirect=True)
def test_check_payload(load_payload):
    payload, _ = load_payload
    assert payload is not None
    assert "job" in payload