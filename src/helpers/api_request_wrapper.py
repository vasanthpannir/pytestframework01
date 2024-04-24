# To make Put,Patch,Get, Delete Requests
import json

import requests


def get_request(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response


def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if post_response is in_json:
        return post_response.json()
    return post_response


def put_request(url, auth, headers, payload, in_json):
    put_response = requests.put(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if put_response is in_json:
        return put_response.json()
    return put_response


def patch_request(url, auth, headers, payload, in_json):
    patch_response = requests.patch(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if patch_response is in_json:
        return patch_response.json()
    return patch_response


def delete_request(url, auth, headers, payload, in_json):
    delete_response = requests.post(url=url, auth=auth, headers=headers, data=json.dumps(payload))
    if delete_response is in_json:
        return delete_response.json()
    return delete_response




