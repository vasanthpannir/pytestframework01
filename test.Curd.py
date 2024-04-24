import requests
from src.helpers.utils import common_headers_json, common_headers_for_put
from src.helpers.payload_manager import payload_create_booking, payload_create_token


def put_request(url, headers, auth, payload, in_json=True):
    response = requests.put(url=url, headers=headers, auth=auth, json=payload)
    return response


put_url = "https://restful-booker.herokuapp.com/booking/2674"
common_headers = common_headers_for_put()
username = "admin"  # Replace with your actual username
password = "password123"  # Replace with your actual password
payload = payload_create_booking()

response = put_request(url=put_url, headers=common_headers, auth=(username, password), payload=payload)

if response.status_code == 200:
    json_data = response.json()
else:
    print("Error:", response.status_code)
