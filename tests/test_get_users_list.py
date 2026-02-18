import requests
import pytest

BASE_URL = "https://reqres.in"
ENDPOINT = "/api/users?page=2"

response = requests.get(f"{BASE_URL}/{ENDPOINT}").json()
# r = response.json()
# print(r)
print(response)

def test_get_users_list():
    response = requests.get(f"{BASE_URL}/{ENDPOINT}")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    data = response.json()
    assert "data" in data, "'data' key not found in response"
    assert isinstance(data["data"], list), "'data' is not a list"
    assert len(data["data"]) > 0, "'data' list is empty"
    
    for user in data["data"]:
        assert "id" in user, "'id' key not found in user"
        assert "email" in user, "'email' key not found in user"
        assert "first_name" in user, "'first_name' key not found in user"
        assert "last_name" in user, "'last_name' key not found in user"
        assert "avatar" in user, "'avatar' key not found in user"
        
        assert isinstance(user["id"], int), "'id' is not an integer"
        assert isinstance(user["email"], str), "'email' is not a string"
        assert isinstance(user["first_name"], str), "'first_name' is not a string"
        assert isinstance(user["last_name"], str), "'last_name' is not a string"
        assert isinstance(user["avatar"], str), "'avatar' is not a string"
        
        assert "@" in user["email"], f"Invalid email format: {user['email']}"


def test_response_time_less_than_500ms():
    response = requests.get(f"{BASE_URL}/{ENDPOINT}")
    assert response.elapsed.total_seconds() < 0.5, f"Response time is too high: {response.elapsed.total_seconds()} seconds"
    print(response)