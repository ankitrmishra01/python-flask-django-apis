#A program that creates a web application that supports AJAX requests and updates the page without reloading.
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/update", methods=["POST"])
def update():
    data = request.json  # Get JSON data from AJAX request
    name = data.get("name", "Guest")
    return jsonify(message=f"Hello, {name}!")

if __name__ == "__main__":
    app.run(debug=True)
