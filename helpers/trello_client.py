import requests

from config import API_KEY, API_TOKEN, BASE_URL


class ApiClient:
    def __init__(self):
        self.key = API_KEY
        self.token = API_TOKEN
        self.base_url = BASE_URL
    

    def create_board(self, name):
        params = {"name": name, "key": self.key,"token": self.token}
        return requests.post(f"{self.base_url}boards/", params=params)
    
    def get_board(self, board_id):
        params = {"key": self.key,"token": self.token}
        return requests.get(f"{self.base_url}boards/{board_id}", params=params)
    
    def delete_board(self, board_id):
        params = {"key": self.key,"token": self.token}
        return requests.delete(f"{self.base_url}boards/{board_id}", params=params)