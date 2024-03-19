import pytest
from src.Helpers.Api_wrapper import post_request
from src.Constants.api_constants import APIConstants
from src.Helpers.utils import common_headers_json
from src.Helpers.payloadmanager import payload_manager
from src.Helpers.Commonverfication import verify_response, verify_http_status_code


class TestCreatebookingTC1:

    def test_createbooking_tc1(self):
        response = post_request(url=APIConstants.url_create_booking(), auth=None, headers=common_headers_json(),
                                payload=payload_manager(), in_json=False)

        print(response.json())

        verify_response(response.json()["bookingid"])
        verify_http_status_code(response, 200)
        print(response.json()["bookingid"])
