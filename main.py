from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """
    This is the default route for the app.
    """
    return "<h1>Hello, world!</h1>"

if __name__ == '__main__':
    app.run(port=4050, host="0.0.0.0")

    