import datetime
import json
import logging
import os
import pickle

import requests

CONFIG_JSON = "./turnip_exchange_config.json"

PAYLOAD = {"category": "turnips", "islander": "neither"}
TURNIP_EXCHANGE_URL = "https://api.turnip.exchange/islands/"
DEBUG = True
HERE = os.path.abspath(os.path.dirname(__file__))

log = logging.getLogger(__name__)


def request_data(file_path=None):
    log.debug(f"Loading from {file_path}")
    if file_path:
        response = load_response_from_file(file_path)
    else:
        response = _make_request()
    log.debug(f"Response Headers: {response.headers}")
    return json.loads(response.text)


def _make_request():
    log.debug("Making live request!")
    return (requests.post(
        TURNIP_EXCHANGE_URL,
        json=PAYLOAD,
        headers=_get_config_value('headers'),
        cookies=_get_config_value('cookies'),
    ))


def _get_config_value(key):
    print(os.path.join(HERE, CONFIG_JSON))
    with open(os.path.join(HERE, CONFIG_JSON), "r") as _config:
        return json.load(_config)[key]


def write_response_to_file(response, file_path):
    pickle.dump(response, open(file_path, "wb"))


def load_response_from_file(file_path):
    return pickle.load(open(file_path, "rb"))


def write_json_data_to_file(response, file_path):
    with open(file_path, "w", encoding="utf-8") as _file:
        json.dump(json.loads(response.text), _file)


def read_json_data_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as _file:
        return _file.readlines()


def datetime_now(delta: datetime.timedelta = None):
    """Returns datetime string

    .. example:: 2020-01-01 23:59:59

    Returns:
         `str`
    """

    return str(datetime.datetime.now() + delta)[:19]


def date_now(delta: datetime.timedelta = None):
    """Returns date string

    .. example:: 2020-01-01

    Returns:
        `str`

    """
    return str(datetime.datetime.now() + delta)[:10]


""" TODO
Check success in request
Check success in json response
Incorporate $$time
Create object that stores

payload should not be static
"""
