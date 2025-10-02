import pytest

def test_check_base_and_config(base_url, load_config, load_expectation):
    assert base_url == "https://jsonplaceholder.typicode.com/"
    config = load_config["endpoints"]  # Accede al nesting
    assert "posts_get" in config
    exp = load_expectation
    assert exp["posts_get"]["status_code"] == 200

@pytest.mark.parametrize("load_payload", ["posts_post"], indirect=True)
def test_check_payload(load_payload):
    payload, _ = load_payload
    assert payload is not None
    assert "title" in payload