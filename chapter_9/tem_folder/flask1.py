from flask import Flask


app= Flask(__name__)

@app.route('/')
def hello_networkers():
    return 'Hello networkers'

if __name__ == '__main__':
    app.run(debug=True)
