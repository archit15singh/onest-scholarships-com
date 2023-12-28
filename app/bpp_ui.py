import requests

# BPP's search API endpoint
bpp_search_url = "http://localhost:5002/search"

# Example fake data for the search action
fake_search_data = {
    "query": "Artificial Intelligence",
    "filters": {"level": "intermediate", "category": "AI"},
}

# Call BPP's search API
response = requests.post(bpp_search_url, json=fake_search_data)

# Print the response from BPP
print("BPP's response:", response.json())
