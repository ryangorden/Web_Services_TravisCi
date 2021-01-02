from flask import Flask

app = Flask(__name__)


# The is a simple endpoint url
# that return a simple string
@app.route('/')
def index():
    return 'You are at index()'

# The is demo the creation of an
# second endpoint.
@app.route('/routers/')
def routers():
    return 'You are at routers()'


if __name__ == '__main__':
    app.run(debug=True)
