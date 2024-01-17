from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)
port = 3000


@app.route("/on_subscribe", methods=["POST"])
def on_subscribe():
    print("Received a subscription request:", request.json)
    return jsonify({"message": "Subscription successful"})


@app.route("/client_callback", methods=["POST"])
def client_callback():
    print("Received a response for client_callback:", request.json)
    return jsonify({"message": "successful"})


@app.route("/search", methods=["POST"])
def search():
    try:
        request_data = {
            "context": request.json.get("context", {}),
            "message": request.json.get("message", {}),
        }
        response = requests.post("http://localhost:5000/search", json=request_data)
        print("got the data from /search", response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


@app.route("/select", methods=["POST"])
def select():
    try:
        request_data = {
            "context": request.json.get("context", {}),
            "message": request.json.get("message", {}),
        }
        response = requests.post("http://localhost:5000/select", json=request_data)
        print("got the data from /select", response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


@app.route("/init", methods=["POST"])
def init():
    try:
        request_data = {
            "context": request.json.get("context", {}),
            "message": request.json.get("message", {}),
        }
        response = requests.post("http://localhost:5000/init", json=request_data)
        print("got the data from /init", response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


if __name__ == "__main__":
    app.run(port=port, debug=True)
