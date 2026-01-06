# tests/test_api_basics.py
import requests

#----------------------------------------------------------
# LEARNING NOTE: 
# GET = Read (Ask for data)
#Post = Create (Send new data to the server)
#----------------------------------------------------------

# TEST CASE 1: Happy Path (GET 200)
def test_get_status_code_200():
    print("\n--- Test 1: Happy Path(Read) ---")
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200

# TEST 2: Sad Path (GET 404)
def test_get_status_code_404():
    print("\n--- Test 2: Sad Path (Missing) ---")
    url = "https://jsonplaceholder.typicode.com/post/99999"
    response = requests.get(url)
    assert response.status_code == 404

# TEST 3: Ceate New Data (POST 201)
def test_post_create_new_data():
    print("\n--- Test 3: Create DATA (POST) ---")

    # 1. ARRANGE
    url = "https://jsonplaceholder.typicode.com/posts"

    # The Payload: the data we want to send
    my_new_post = {
        "title": "QA Automation Engineer",
        "body": "i am learning to automate APIs with Python",
        "userId": 1
    }

    # 2. ACT
    response = requests.post(url, json=my_new_post)

    # 3. ASSERT
    #Status 201 means "Successfully Created"
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 201

    # Verify the server returned our data
    data = response.json()
    print(f"Server Response: {data}")
    assert data ["title"] == "QA Automation Engineer"