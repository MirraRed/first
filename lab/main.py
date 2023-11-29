from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/hello-world-<int:variant>')
def hello_world(variant):
    message = f'Hello World {variant}'
    return message, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)