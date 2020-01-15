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

def test_hello_json(api):
    arg = 'morake'
    r = api.requests.get(f'/hello/{arg}/json')
    assert 'content-type' in r.headers
    assert r.headers['content-type'] == 'application/json'
    r_json = r.json()
    assert 'message' in r_json
    assert r_json['message'] == f'hello, {arg}'

def test_hello_html(api):
    arg = 'morake'
    r = api.requests.get(f'/hello/{arg}/html')
    assert 'content-type' in r.headers
    assert r.headers['content-type'] == 'text/html'

def test_teapot(api):
    r = api.requests.get('/416')
    assert r.status_code == 416

def test_pizza_pizza(api):
    r = api.requests.get('/pizza')
    assert 'X-pizza' in r.headers
    assert r.headers['X-Pizza'] == '42'
