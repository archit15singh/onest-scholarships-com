# BPP Server (initiating actions):
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


# Endpoint to initiate search action
@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    # Perform the search action
    # For simplicity, just print the received data
    print("BPP initiating search action:", data)
    # Assuming BAP's URL is known, you can trigger on_search here
    bap_url = "http://localhost:5001/on_search"
    response = requests.post(bap_url, json=data)
    return response.json()


if __name__ == "__main__":
    app.run(port=5002)
