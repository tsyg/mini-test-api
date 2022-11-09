# https://docs.pytest.org/en/7.1.x/example/simple.html
import requests
import pytest

host_url = "https://www.w3.org/"


def test_anonymous_page_open():
    response = requests.get(url=host_url)
    assert response.status_code == 200


@pytest.mark.parametrize("username, password", [
    ("badname", "not-a-password"),
    ("AnotherBadOne", "123")
])
def test_wrong_credentials(username, password):
    response = requests.post(url=host_url, data=f"j_username={username}&j_password={password}")
    print(response.text)
    assert response.status_code in [401, 403]

