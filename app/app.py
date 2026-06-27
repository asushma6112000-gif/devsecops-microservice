from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Python Microservice Running"

@app.route("/health")
def health():
    return jsonify(status="UP", service="python-microservice")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
