import requests
import json

class GetRequester:
    def __init__(self, url: str):
        self.url = url

    def get_response_body(self) -> str:
        response = requests.get(self.url)
        response.raise_for_status() 
        return response.text  

    def load_json(self) -> dict:
        response_body = self.get_response_body()
        return response.json()  