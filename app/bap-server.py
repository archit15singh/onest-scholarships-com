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


def print_human_readable(json_object):
    """
    This function takes a JSON object and prints its contents in a human-readable format,
    focusing on individual items.
    """
    context = json_object["context"]
    responses = json_object["responses"]

    # Print context information
    print("Context:")
    print(f"  Action: {context['action']}")
    print(f"  Message ID: {context['message_id']}")
    print(f"  Transaction ID: {context['transaction_id']}")
    print(f"  Domain: {context['domain']}")
    print(
        f"  Location: {context['location']['city']['name']}, {context['location']['country']['name']}"
    )
    print()

    # Iterate through responses
    for response in responses:
        print("Response:")
        response_context = response["context"]
        message = response["message"]

        # Print response context information
        print(f"  Domain: {response_context['domain']}")
        print(f"  Action: {response_context['action']}")
        print(f"  Provider ID: {response_context['bpp_id']}")
        print(
            f"  Location: {response_context['location']['city']['name']}, {response_context['location']['country']['name']}"
        )
        print()

        # Print order details
        order = message["order"]
        print("Order Details:")
        print(f"  Order Type: {order['type']}")
        print(f"  Provider Name: {order['provider']['descriptor']['name']}")
        for item in order["items"]:
            print(f"    Item Name: {item['descriptor']['name']}")
            print(f"    Price: {item['price']['value']} {item['price']['currency']}")
            for tag in item["tags"]:
                print(f"    Tag: {tag['descriptor']['name']}")
                for detail in tag["list"]:
                    print(
                        f"      Detail: {detail['descriptor']['name']} - {detail['value']}"
                    )
        print()


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


@app.route("/select", methods=["POST"])
def select():
    try:
        request_data = {
            "context": request.json.get("context", {}),
            "message": request.json.get("message", {}),
        }
        response = requests.post("http://localhost:5000/select", json=request_data)
        print("got the data from /select", response.json())
        print_human_readable(response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


if __name__ == "__main__":
    app.run(port=port, debug=True)
