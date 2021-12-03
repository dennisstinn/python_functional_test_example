import pytest
import json
import logging

def pytest_configure():
    # import config parameters from config.json file

    # get enviroment file
    env = 'stage'

    # read the data from the file into a dictionary
    with open('config.json') as f:
        json_config = json.loads(f.read())

    # return configuration based on env
    for config_env in json_config['env']:
        if config_env['name'] == env:
            pytest.cfg = config_env



    logging.basicConfig(level=logging.INFO)


