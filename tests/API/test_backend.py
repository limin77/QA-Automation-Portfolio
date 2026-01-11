import pytest
import requests

# NEW TARGET: JSONPlaceholder (Friendly to Automation)
BASE_URL = "https://jsonplaceholder.typicode.com"

class TestBackendAPI:
    
    @pytest.mark.api
    def test_health_check_200(self):
        """
        Verify the server is UP and returns posts.
        """
        endpoint = f"{BASE_URL}/posts"
        
        # This API is friendly, we don't even need headers
        response = requests.get(endpoint)
        
        # Verify 200 OK
        assert response.status_code == 200, f"Server Error! Got: {response.status_code}"
        
        # Verify we got a list of posts
        data = response.json()
        assert len(data) > 0
        print(f"API Success: Retrieved {len(data)} posts.")

    @pytest.mark.api
    def test_create_post_simulation(self):
        """
        Verify we can CREATE data (POST).
        """
        endpoint = f"{BASE_URL}/posts"
        payload = {
            "title": "Alimin QA Project",
            "body": "Testing Automation",
            "userId": 1
        }
        
        response = requests.post(endpoint, json=payload)
        
        # JSONPlaceholder returns 201 for Created
        assert response.status_code == 201, f"Failed! Got: {response.status_code}"
        
        # Verify the data came back
        data = response.json()
        assert data["title"] == "Alimin QA Project"
        print(f"API Success: Created Post ID {data['id']}")