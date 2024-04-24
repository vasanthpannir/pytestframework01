# Common Headers

def common_headers_json():
    headers = {
        "content-Type": "application/json"
    }
    return headers


def common_headers_xml():
    headers = {
        "content-Type": "application/xml"
    }
    return headers


def common_headers_for_put_delete_patch():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=",
    }
    return headers
