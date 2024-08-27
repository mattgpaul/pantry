import os
import requests

class PaprikaClient:
    def __init__(self):
        self.base_url = "https://paprikaapp.com/api/v2"
        self.email = os.getenv("PAPRIKA_EMAIL")
        self.password = os.getenv("PAPRIKA_PASSWORD")
        self.auth_token = None
        self.session = requests.Session()

    def authenticate(self):
        url = f"{self.base_url}/account/login"
        payload = {
            "email": self.email,
            "password": self.password
        }
        
        response = self.session.post(url, data=payload)
        response.raise_for_status()
        self.auth_token = response.json().get("result", {}).get("token")
        return self.auth_token

    def get_recipes(self):
        url = f"{self.base_url}/sync/recipes"
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }
        
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_recipe_details(self, uid):
        url = f"{self.base_url}/sync/recipe/{uid}"
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }
        
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def get_groceries(self):
        url = f"{self.base_url}/sync/groceries"
        headers = {
            "Authorization": f"Bearer {self.auth_token}"
        }
        
        response = self.session.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    client = PaprikaClient()
    client.authenticate()  # Ensure authentication before making the request
    groceries = client.get_groceries()
    print(f"Groceries: {groceries}")