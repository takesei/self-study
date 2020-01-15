import pytest
from app.app import api as service

@pytest.fixture
def api():
    return service

def test_root(api):
    r = api.requests.get('/')
    assert r.text == 'hello, world!'
