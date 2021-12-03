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

def test_success1():
    url = pytest.cfg['baseurl']

    response = requests.get(url)
    assert response.status_code == 200, f"Expected 200 response code, Received code: {response.status_code}, body: {response.text}"

    json_response = json.loads(response.text)
    assert len(json_response['cars']) >= 0


