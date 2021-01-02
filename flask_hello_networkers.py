from flask import Flask


app= Flask(__name__)

# The is a simple endpoint url
# that return a simple string
@app.route('/')
def hello_networkers():
    return 'Hello networkers'

if __name__ == '__main__':
    app.run(debug=True)
