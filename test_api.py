import requests
import re
import secrets
import logging



def test_get_all_users():
    url = "http://192.168.31.169:8000/get_all_users"

    logging.info("Sending GET request to /get_all_users")
    response = requests.get(url)

    logging.info(f"Received response with status code: {response.status_code}") 
    assert response.status_code == 200

    logging.info(f"Response data: {response.text}")
    data = response.json()
    print(data)


def test_create_user():
    url = "http://192.168.31.169:8000//create_user"
    payload = {
        "user_name": "Arun Krishna",
        "user_id": 10,
        "email": "arun@gmail.com",
        "city": "Kurnool"
    }

    logging.info("Sending POST request to create user")
    response = requests.post(url, json=payload )


    logging.info(f"Received response with status code: {response.status_code}")
    assert response.status_code == 200

    logging.info(f"Response data: {response.text}")
    data = response.json()
    assert "token" in data
    logging.info(f"Token received: {data['token']}")
    print(response.text)
  

def test_get_user_by_id():
    url = "http://192.168.31.169:8000//get_user/10"
    response = requests.get(url)


    assert response.status_code == 200
    logging.info(f"Received response with status code: {response.status_code}")

    logging.info(f"Response data: {response.text}")
    data = response.json()
    print(data)
    logging.info("Test passed successfully ✅")

