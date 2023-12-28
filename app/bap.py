# BAP Server (reactive):
from flask import Flask, request, jsonify

app = Flask(__name__)


# Endpoint to handle external search action
@app.route("/on_search", methods=["POST"])
def on_search():
    data = request.get_json()
    # Process the search action
    # For simplicity, just print the received data
    print("BAP reacting to search action:", data)
    return jsonify({"message": "Search action processed by BAP"})


if __name__ == "__main__":
    app.run(port=5001)
