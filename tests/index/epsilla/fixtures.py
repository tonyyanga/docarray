import os
import time

import pytest

cur_dir = os.path.dirname(os.path.abspath(__file__))
epsilla_yml = os.path.abspath(os.path.join(cur_dir, 'docker-compose.yml'))

epsilla_config = {
    "protocol": 'http',
    "host": 'localhost',
    "port": 8888,
    "is_self_hosted": True,
    "db_path": "/epsilla",
    "db_name": "tony_doc_array_test",
}


@pytest.fixture(scope='session', autouse=True)
def start_storage():
    os.system(f"docker compose -f {epsilla_yml} up -d --remove-orphans")
    time.sleep(2)

    yield
    os.system(f"docker compose -f {epsilla_yml} down --remove-orphans")
