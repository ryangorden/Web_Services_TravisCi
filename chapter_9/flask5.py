from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'You are at index()'

@app.route('/routers/<hostname>')
def routers(hostname):
    return f'You are at {hostname}'

@app.route('/routers/<hostname>/interface/<int:interface_number>')
def interface(hostname, interface_number):
    return jsonify(name=hostname, interface=interface_number)

@app.route('/switches/<hostname>/list_interfaces')
def devices(hostname):
    if hostname in switches:
        return f'Listing interfaces for {hostname}'
    else:
        return 'Invalid hostname', 404

switches= ['s1', 's2', 's3']


if __name__ == '__main__':
    app.run(debug=True)