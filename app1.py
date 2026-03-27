from flask import Flask, make_response
app = Flask(__name__)
@app.route("/")
def home():
    resp = make_response("Hello app1")
    resp.headers["CustomHeader"] = "demo"
    return resp
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5001)

