from flask import Flask

app = Flask(__name__)

# The is a simple endpoint url
# that return a simple string
@app.route('/')
def index():
    return 'You are at index()'

# The is endpoint url takes a dynamic url
# then return that router hostname
@app.route('/routers/<hostname>')
def routers(hostname):
    return f'You are at {hostname}'

# This endpoint url in takes a dynamic hostname and interface number 
# in url path then return the hostname and interface.
@app.route('/routers/<hostname>/interface/<int:interface_number>')
def interface(hostname, interface_number):
    return f'You are at interface {interface_number} on {hostname}'


if __name__ == '__main__':
    app.run(debug=True)
