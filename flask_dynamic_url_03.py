from flask import Flask, url_for

app = Flask(__name__)

# The is a simple endpoint url
# that return a simple string
@app.route('/')
def index():
    return 'You are at index()'

# This endpoint url in takes a dynamic hostname in the url path
# Then return the hostname to  the screen.
@app.route('/routers/<hostname>')
def routers(hostname):
    return f'You are at {hostname}'

# This endpoint url in takes a dynamic hostname and interface number 
# in url path then return the hostname and interface.
@app.route('/routers/<hostname>/interface/<int:interface_number>')
def interface(hostname, interface_number):
    return f'You are at interface {interface_number} on {hostname}'

# This endpoint url in takes a dynamic hostname 
# in url path then if hostname in lst hostname will
# be displayed.
@app.route('/switches/<hostname>/list_interfaces')
def devices(hostname):
    if hostname in switches:
        return f'Listing interfaces for {hostname}'
    else:
        return 'Invalid hostname', 404

switches= ['s1', 's2', 's3']

for switch in switches:
    with app.test_request_context():
        print(url_for('devices', hostname=switch))

if __name__ == '__main__':
    app.run(debug=True)
