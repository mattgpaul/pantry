import pytest
import requests
from src.paprika3.paprika_client import PaprikaClient

@pytest.fixture
def client():
    client = PaprikaClient()
    client.auth_token = "fake_token"
    return client

def test_authenticate(mocker, client):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"result": {"token": "fake_token"}}
    mock_response.raise_for_status = mocker.Mock()
    mocker.patch('requests.Session.post', return_value=mock_response)

    token = client.authenticate()
    assert token == "fake_token"
    requests.Session.post.assert_called_once_with(
        f"{client.base_url}/account/login",
        data={"email": client.email, "password": client.password}
    )

def test_get_recipes(mocker, client):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"result": [{"uid": "1", "hash": "abc"}]}
    mock_response.raise_for_status = mocker.Mock()
    mocker.patch('requests.Session.get', return_value=mock_response)