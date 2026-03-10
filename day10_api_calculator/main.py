from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Day 10 API Calculator"

@app.route("/add")
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": a + b})

@app.route("/subtract")
def subtract():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": a - b})

@app.route("/multiply")
def multiply():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": a * b})

@app.route("/divide")
def divide():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))

    if b == 0:
        return jsonify({"error": "Division by zero not allowed"})

    return jsonify({"result": a / b})

if __name__ == "__main__":
    app.run(debug=True)
