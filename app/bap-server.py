from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)
port = 3000


def process_response(data):
    if not data or "responses" not in data or not isinstance(data["responses"], list):
        print("Invalid data structure")
        return

    for response in data["responses"]:
        providers = response.get("message", {}).get("catalog", {}).get("providers", [])
        if not providers or not isinstance(providers, list):
            print("Invalid or missing providers array in response")
            continue

        for provider in providers:
            print(f"Provider: {provider['descriptor']['name']}")
            for item in provider["items"]:
                print(f"  Scholarship Name: {item['descriptor']['name']}")
                print(f"  Description: {item['descriptor']['long_desc']}")
                print(f"  Amount: {item['price']['value']} {item['price']['currency']}")
                for tag in item["tags"]:
                    print(f"  Tag - {tag['descriptor']['name']}:")
                    for listItem in tag["list"]:
                        print(
                            f"    {listItem['descriptor']['name']}: {listItem['value']}"
                        )
                print(
                    f"  Application Start: {find_date(provider['fulfillments'], 'APPLICATION-START')}"
                )
                print(
                    f"  Application End: {find_date(provider['fulfillments'], 'APPLICATION-END')}"
                )
                print("")


def find_date(fulfillments, type):
    if not fulfillments or not isinstance(fulfillments, list):
        return "Not specified"

    for fulfillment in fulfillments:
        for stop in fulfillment["stops"]:
            if stop["type"] == type:
                timestamp = stop["time"]["timestamp"]
                if timestamp.endswith("Z"):
                    timestamp = timestamp[:-1] + "+00:00"
                return datetime.fromisoformat(timestamp).strftime("%Y-%m-%d")
    return "Not specified"


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
        process_response(response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


if __name__ == "__main__":
    app.run(port=port, debug=True)
