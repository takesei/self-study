import responder

api = responder.API()

@api.route('/')
def root(req, resp):
    resp.text = 'hello, world!'

@api.route('/hello/{who}')
def root(req, resp, *, who):
    resp.text = f'hello, {who}!'

if __name__ == '__main__':
    api.run()
