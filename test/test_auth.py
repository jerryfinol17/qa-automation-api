import pytest
import requests
import allure
from allure import step, attach

endpoints_auth = ["auth_register_valid","auth_register_invalid","auth_login_valid","auth_login_invalid"]

@pytest.mark.parametrize("load_auth_payload",endpoints_auth,indirect=True)
def test_auth_register_login(base_url, load_config,load_auth_payload,load_auth_expectation):
	payload, endpoint = load_auth_payload
	config_key = "_".join(endpoint.split("_")[:2])
	config = load_config["endpoints"][config_key]
	expected = load_auth_expectation[endpoint]
	url = base_url + config["path"]
	headers = {"x-api-key": "reqres-free-v1"}

	with step(f"Execute {config['method']}{endpoint} to {url} with payload: {payload}"):
		response = requests.post(url, json=payload, headers=headers)
		attach(response.text, "Response Body", attachment_type=allure.attachment_type.JSON)

	with step(f"Validate {endpoint} response"):
		assert response.status_code == expected["status_code"]
		data = response.json()
		assert all(key in data for key in expected["required_keys"])

	if "auth_login_valid" in endpoint:
		token = data["token"]
		with step(f"Execute protected GET / users with Bearer{token[:10]}..."):
			protected_headers = {"Authorization": f"Bearer {token}",**headers}
			protected_response = requests.get(base_url + "/users", headers=protected_headers)
			attach(protected_response.text, "Protected Response", attachment_type=allure.attachment_type.JSON)
			assert protected_response.status_code == 200
			protected_data = protected_response.json()
			assert "data" in protected_data and len(protected_data["data"]) > 0