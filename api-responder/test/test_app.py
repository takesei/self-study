import pytest
from app.app import api as service

@pytest.fixture
def api():
    return service

def test_root(api):
    r = api.requests.get('/')
    assert r.text == 'hello, world!'

def test_hello(api):
    arg = 'honya'
    r = api.requests.get(f'/hello/{arg}')
    assert r.text == f'hello, {arg}!'
