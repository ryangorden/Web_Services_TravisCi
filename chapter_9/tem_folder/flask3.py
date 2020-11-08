from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'You are at index()'

@app.route('/routers/<hostname>')
def routers(hostname):
    return f'You are at {hostname}'

@app.route('/routers/<hostname>/interface/<int:interface_number>')
def interface(hostname, interface_number):
    return f'You are at interface {interface_number} on {hostname}'


if __name__ == '__main__':
    app.run(debug=True)