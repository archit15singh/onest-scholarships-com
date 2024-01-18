from flask import Flask, request, jsonify, render_template, redirect, url_for, session
import requests
import datetime

app = Flask(__name__)
app.secret_key = "b1c012a6-ab62-4230-83f5-50702cb3097e"
port = 3000

BAP_ID = "2fe7-2405-201-800b-c21a-2538-43c5-6514-4340.ngrok-free.app"
BAP_URI = "https://2fe7-2405-201-800b-c21a-2538-43c5-6514-4340.ngrok-free.app/"


def create_request_body_for_search(search_string):
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
            "transaction_id": "a8aaecca-10b7-4d19-b640-022723112309",
            "message_id": "a7aaecca-10b7-4d19-b640-b047a7c60009",
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "ttl": "PT10M",
        },
        "message": {"intent": {"item": {"descriptor": {"name": search_string}}}},
    }
    return request_body


def create_request_body_for_select(scholarship_details):
    bpp_id = scholarship_details.pop("bppId")
    bpp_uri = scholarship_details.pop("bppUri")
    request_body = {
        "context": {
            "domain": "onest:financial-support",
            "location": {
                "city": {"name": "Bangalore", "code": "std:080"},
                "country": {"name": "India", "code": "IND"},
            },
            "action": "select",
            "version": "1.1.0",
            "bap_id": BAP_ID,
            "bap_uri": BAP_URI,
            "bpp_id": bpp_id,
            "bpp_uri": "https://" + bpp_id,
            "transaction_id": "a8aaecca-10b7-4d19-b640-022723112309",
            "message_id": "a7aaecca-10b7-4d19-b640-b047a7c60009",
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "ttl": "PT10M",
        },
        "message": {"order": scholarship_details},
    }
    return request_body


def create_request_body_for_init(order_details):
    bpp_id = order_details.pop("bpp_id")
    bpp_uri = order_details.pop("bpp_uri")
    request_body = {
        "context": {
            "domain": "onest:financial-support",
            "location": {
                "city": {"name": "Bangalore", "code": "std:080"},
                "country": {"name": "India", "code": "IND"},
            },
            "action": "init",
            "version": "1.1.0",
            "bap_id": BAP_ID,
            "bap_uri": BAP_URI,
            "bpp_id": bpp_id,
            "bpp_uri": bpp_uri,
            "transaction_id": "a8aaecca-10b7-4d19-b640-022723112309",
            "message_id": "a7aaecca-10b7-4d19-b640-b047a7c60009",
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "ttl": "PT10M",
        },
        "message": {"order": order_details},
    }
    return request_body


def create_request_body_for_confirm(order_details):
    bpp_id = order_details.pop("bpp_id")
    bpp_uri = order_details.pop("bpp_uri")
    request_body = {
        "context": {
            "domain": "onest:financial-support",
            "location": {
                "city": {"name": "Bangalore", "code": "std:080"},
                "country": {"name": "India", "code": "IND"},
            },
            "action": "confirm",
            "version": "1.1.0",
            "bap_id": BAP_ID,
            "bap_uri": BAP_URI,
            "bpp_id": bpp_id,
            "bpp_uri": bpp_uri,
            "transaction_id": "a8aaecca-10b7-4d19-b640-022723112309",
            "message_id": "a7aaecca-10b7-4d19-b640-b047a7c60009",
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "ttl": "PT10M",
        },
        "message": {"order": order_details},
    }
    return request_body


def create_request_body_for_status(order_details):
    bpp_id = order_details.pop("bpp_id")
    bpp_uri = order_details.pop("bpp_uri")
    request_body = {
        "context": {
            "domain": "onest:financial-support",
            "location": {
                "city": {"name": "Bangalore", "code": "std:080"},
                "country": {"name": "India", "code": "IND"},
            },
            "action": "status",
            "version": "1.1.0",
            "bap_id": BAP_ID,
            "bap_uri": BAP_URI,
            "bpp_id": bpp_id,
            "bpp_uri": bpp_uri,
            "transaction_id": "a8aaecca-10b7-4d19-b640-022723112309",
            "message_id": "a7aaecca-10b7-4d19-b640-b047a7c60009",
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "ttl": "PT10M",
        },
        "message": order_details,
    }
    return request_body


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/details", methods=["GET", "POST"])
def details():
    if request.method == "POST":
        session["scholarship_details"] = request.get_json()
        return redirect(url_for("details"))
    scholarship_details = session.get("scholarship_details", {})
    return render_template("details.html", scholarship_details=scholarship_details)


@app.route("/init_details")
def init_details():
    return render_template("init_details.html")


@app.route("/client_callback", methods=["POST"])
def client_callback():
    print("Received a response for client_callback:", request.json)
    return jsonify({"message": "successful"})


@app.route("/confirm_details")
def confirm_details():
    return render_template("confirm_details.html")


@app.route("/status_details")
def status_details():
    return render_template("status_details.html")


@app.route("/search", methods=["POST"])
def search():
    try:
        search_string = request.get_json().get("searchQuery")
        request_data = create_request_body_for_search(search_string)
        # request_data = {
        #     "context": request.json.get("context", {}),
        #     "message": request.json.get("message", {}),
        # }
        response = requests.post("http://localhost:5000/search", json=request_data)
        print("got the data from /search", response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


@app.route("/select", methods=["POST"])
def select():
    try:
        scholarship_details = request.json
        request_data = create_request_body_for_select(scholarship_details)
        # request_data = {
        #     "context": request.json.get("context", {}),
        #     "message": request.json.get("message", {}),
        # }
        response = requests.post("http://localhost:5000/select", json=request_data)
        print("got the data from /select", response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


@app.route("/init", methods=["POST"])
def init():
    try:
        order_details = request.json
        request_data = create_request_body_for_init(order_details)
        print(request_data, "\n\n")
        # request_data = {
        #     "context": request.json.get("context", {}),
        #     "message": request.json.get("message", {}),
        # }
        response = requests.post("http://localhost:5000/init", json=request_data)
        print("got the data from /init", response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


@app.route("/confirm", methods=["POST"])
def confirm():
    try:
        order_details = request.json
        request_data = create_request_body_for_confirm(order_details)
        print(request_data, "\n\n")
        # request_data = {
        #     "context": request.json.get("context", {}),
        #     "message": request.json.get("message", {}),
        # }
        response = requests.post("http://localhost:5000/confirm", json=request_data)
        print("got the data from /confirm", response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


@app.route("/status", methods=["POST"])
def status():
    try:
        order_details = request.json
        request_data = create_request_body_for_status(order_details)
        print(request_data, "\n\n")
        # request_data = {
        #     "context": request.json.get("context", {}),
        #     "message": request.json.get("message", {}),
        # }
        response = requests.post("http://localhost:5000/status", json=request_data)
        print("got the data from /status", response.json())
        return jsonify(response.json())
    except Exception as error:
        print("Error calling external API", error)
        return jsonify({"error": "Error calling external API"}), 500


if __name__ == "__main__":
    app.run(port=port, debug=True)
