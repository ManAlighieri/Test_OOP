from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run(host='10.2.80.252', port=5000)