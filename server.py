from flask import Flask, Response

app = Flask(__name__)

@app.route('/', methods='GET')
def index():
    status_code = Response(status=200)
    return status_code

if __name__ == "__main__":
    app.run(debug=True)
