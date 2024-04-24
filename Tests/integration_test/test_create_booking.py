import pytest
import requests
from src.constants.api_constants import APIconstants
from src.helpers.api_request_wrapper import post_request
from src.helpers.utils import common_headers_json
from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.payload_manager import payload_create_booking


class TestCreateBooking():
     @pytest.mark.postive
    def test_create_booking_tc1(self):
        response = post_request(url=APIconstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                payload=payload_create_booking()
                                , in_json=False)
        print(response)
        verify_response_key_should_not_be_none(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        print(response.json()['bookingid'])

    @pytest.mark.negative
    def test_create_booking_tc2(self):
        response = post_request(url=APIconstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                payload={}
                                , in_json=False)
        print(response)
        verify_http_status_code(response, 500)

