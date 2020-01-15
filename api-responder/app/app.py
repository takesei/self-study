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

@api.route('/pizza')
def pizza_pizza(req, resp):
    resp.headers['X-Pizza'] = '42'

@api.route('/incoming')
async def receive_incoming(req, resp):
    @api.background.task
    def process_data(data):
        'demo part'
        time.sleep(10)
    data = await req.media()
    process_data(data)
    resp.media = {'success': True}

@api.route('/file-upload')
async def upload_file(req, resp):
    @api.background.task
    def process_data(data):
        f = open('./{}'.format(data['file']['filename']), 'w')
        f.write(data['file']['content'].decode('utf-8'))
        f.close()

    data = await req.media(format='files')
    process_data(data)

    resp.media = {'success': 'ok'}

