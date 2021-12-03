from datetime import datetime
import pytest
import json
import requests
import logging

@pytest.fixture(autouse=True)
def run_around_tests():
    # start of test
    start_time = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    logging.info(f"starting test: {start_time}")

    yield

    # end of the test
    end_time = datetime.now().strftime("%Y-%m-%d, %H:%M:%S")
    logging.info(f"end test: {end_time}")

def test_success():
    url = pytest.cfg['baseurl']
    data = {"model": "AAA", "year": "1111", "miles": 2000}

    response = requests.post(url, data=json.dumps(data))
    assert response.status_code == 200, f"Expected 200 response code, Received code: {response.status_code}, body: {response.text}"

    json_response = json.loads(response.text)
    assert json_response['model'] == data['model']
    assert json_response['year'] == data['year']
    assert json_response['miles'] == data['miles']


def test_requires_model():
    url = pytest.cfg['baseurl']
    data = {"year": "1111", "miles": 2000}

    response = requests.post(url, data=json.dumps(data))
    assert response.status_code == 403, f"Expected 200 response code, Received code: {response.status_code}, body: {response.text}"
    assert response.text == 'Error model not found'


def test_requires_year():
    url = pytest.cfg['baseurl']
    data = {"model": "AAA", "miles": 2000}

    response = requests.post(url, data=json.dumps(data))
    assert response.status_code == 403, f"Expected 200 response code, Received code: {response.status_code}, body: {response.text}"
    assert response.text == 'Error year not found'


def test_requires_miles():
    url = pytest.cfg['baseurl']
    data = {"model": "AAA", "year": "1111"}

    response = requests.post(url, data=json.dumps(data))
    assert response.status_code == 403, f"Expected 200 response code, Received code: {response.status_code}, body: {response.text}"
    assert response.text == 'Error miles not found'


