import responder

api = responder.API()

@api.route('/')
def root(req, resp):
    resp.text = 'hello, world!'

@api.route('/hello/{who}')
def hello(req, resp, *, who):
    resp.text = f'hello, {who}!'

@api.route('/hello/{who}/json')
def hello_json(req, resp, *, who):
    resp.media = {'message': f'hello, {who}'}

@api.route('/hello/{who}/html')
def hello_html(req, resp, *, who):
    resp.html = api.template('hello.html', who=who)

@api.route('/416')
def teapot(req, resp):
    resp.status_code = api.status_codes.HTTP_416
