from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Docker CI/CD Pipeline"

app.run(host="0.0.0.0", port=8080)
