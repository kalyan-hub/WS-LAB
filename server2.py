from flask import Flask, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/data')
def data():
    return Response('Data from Server 2', content_type='text/plain')

if __name__ == '__main__':
    app.run(port=8001)
