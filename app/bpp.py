# bpp.py
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

    # Process BAP's response
    bap_response_data = response.json()
    search_results = bap_response_data.get("search_results", [])

    # Simulate further processing of search results by BPP
    selected_course = search_results[0] if search_results else None
    quote = 150.00  # Simulated quote for the selected course

    return jsonify(
        {
            "message": "Search action processed by BPP",
            "selected_course": selected_course,
            "quote": quote,
        }
    )


if __name__ == "__main__":
    app.run(port=5002)
