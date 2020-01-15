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

if __name__ == '__main__':
    api.run()
