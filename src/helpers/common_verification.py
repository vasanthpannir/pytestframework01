# HTTPS status Verification


def verify_http_status_code(response_data, expect_data):
    print(response_data.status_code)
    print(expect_data)
    assert response_data.status_code == expect_data, "Expected HTTP Status Code" + str(expect_data)


def verify_json_key_for_not_null(key):
    assert key != 0, "Key is non Empty" + key
    assert key > 0, "Key is grater than zero"


def verify_response_key_should_not_be_none(key):
    assert key is not None
