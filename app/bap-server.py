from flask import Flask, request, jsonify, render_template
import requests
import datetime
import uuid

app = Flask(__name__)
port = 3000

BAP_ID = "2fe7-2405-201-800b-c21a-2538-43c5-6514-4340.ngrok-free.app"
BAP_URI = "https://2fe7-2405-201-800b-c21a-2538-43c5-6514-4340.ngrok-free.app/"


def create_request_body(search_string):
    request_body = {
        "context": {
            "domain": "onest:financial-support",
            "location": {
                "city": {"name": "Bangalore", "code": "std:080"},
                "country": {"name": "India", "code": "IND"},
            },
            "action": "search",
            "version": "1.1.0",
            "bap_id": BAP_ID,
            "bap_uri": BAP_URI,
            "transaction_id": str(uuid.uuid4()),
            "message_id": str(uuid.uuid4()),
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "ttl": "PT10M",
        },
        "message": {"intent": {"item": {"descriptor": {"name": search_string}}}},
    }
    return request_body


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/client_callback", methods=["POST"])
def client_callback():
    print("Received a response for client_callback:", request.json)
    return jsonify({"message": "successful"})


@app.route("/search", methods=["POST"])
def search():
    try:
        search_string = request.get_json().get("searchQuery")
        request_data = create_request_body(search_string)
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
