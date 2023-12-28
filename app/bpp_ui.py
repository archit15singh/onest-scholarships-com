# bpp_ui.py
import requests

# BPP's search API endpoint
bpp_search_url = "http://localhost:5002/search"

# Example real-world-like data for the search action
realistic_search_data = {
    "query": "Data Science",
    "filters": {"level": "intermediate", "category": "Technology"},
}

# Call BPP's search API
response = requests.post(bpp_search_url, json=realistic_search_data)

# Print the response from BPP
print("BPP's response:", response.json())
