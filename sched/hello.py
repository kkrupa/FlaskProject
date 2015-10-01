from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'


@app.route('/test/')
def helloTest():
    return 'Hello, world! Test!'


if __name__ == '__main__':
    app.run(debug=true)
