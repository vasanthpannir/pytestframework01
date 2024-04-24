import pytest
import requests
import json
from src.constants.api_constants import APIconstants
from src.helpers.api_request_wrapper import post_request, put_request, delete_request
from src.helpers.utils import common_headers_json, common_headers_for_put_delete_patch
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking, payload_create_token


class TestCreateBooking(object):
    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIconstants.url_create_token(), auth=None, payload=payload_create_token(),
                                headers=common_headers_json(),in_json=False)
        verify_http_status_code(response, 200)
        token = response.json()['token']
        print(token)
        verify_response_key_should_not_be_none(token)
        return token


    @pytest.fixture()
    def create_booking(self):
        response = post_request(url=APIconstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                payload=payload_create_booking()
                                , in_json=False)
        print(response)
        booking_id = response.json()['bookingid']
        print(booking_id)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        return booking_id

    def test_update_bookingtc2(self,create_token,create_booking):
        bookingID = create_booking
        put_url = APIconstants.url_create_booking() + str(bookingID)
        response = put_request(url=put_url, headers=common_headers_for_put_delete_patch(), auth=None,
                               payload=payload_create_booking(), in_json=False)
        print(response.json())

    def test_delete_bookingtc3(self):
        # bookingID = create_booking
        username = "admin"
        password = "password123"
        delete_url = APIconstants.url_create_booking() + str("3862")
        response = delete_request(url=delete_url, auth=(username, password),
                                  headers=common_headers_for_put_delete_patch(),payload=payload_create_token(), in_json=False)
        print(response.text)
        print(response.status_code)

