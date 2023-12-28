# bap.py
from flask import Flask, request, jsonify

app = Flask(__name__)


# Endpoint to handle external search action
@app.route("/on_search", methods=["POST"])
def on_search():
    data = request.get_json()
    # Process the search action
    # For simplicity, just print the received data
    print("BAP reacting to search action:", data)

    # Simulate processing and generating search results
    search_results = [
        {
            "course_id": 1,
            "course_name": "Introduction to Machine Learning",
            "provider": "AI Academy",
        },
        {
            "course_id": 2,
            "course_name": "Data Science Fundamentals",
            "provider": "Data Insights",
        },
    ]

    return jsonify(
        {"message": "Search action processed by BAP", "search_results": search_results}
    )


if __name__ == "__main__":
    app.run(port=5001)
