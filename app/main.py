from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)


@app.route('/')
def hello_world():
    return 'Welcome to my app'


@app.route('/status')
def status():
    return '', 204
