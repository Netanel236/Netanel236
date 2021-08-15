from flask import Flask

MESSAGE = "Hello, world! this is app2"

app = Flask(__name__)


@app.route("/app2")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=82)
