from flask import Flask, request, jsonify

app = Flask(__name__)
app.secret_key = "b1c012a6-ab62-4230-83f5-50702cb3097e"
port = 4000

search_object = [
    {
        "context": {
            "domain": "onest:financial-support",
            "action": "on_search",
            "version": "1.1.0",
            "bpp_id": "a8d2-2405-201-800b-c21a-2538-43c5-6514-4340.ngrok-free.app",
            "bpp_uri": "https://a8d2-2405-201-800b-c21a-2538-43c5-6514-4340.ngrok-free.app/",
            "country": "IND",
            "city": "std:080",
            "location": {
                "city": {"name": "Bangalore", "code": "std:080"},
                "country": {"name": "India", "code": "IND"},
            },
            "transaction_id": "a8aaecca-10b7-4d19-b640-022723112309",
            "message_id": "a7aaecca-10b7-4d19-b640-b047a7c60009",
            "ttl": "PT10M",
            "timestamp": "2024-01-24T12:32:41.044Z",
        },
        "message": {
            "catalog": {
                "descriptor": {
                    "name": "Tarka Labs Scholarships and Grants BPP Platform"
                },
                "providers": [
                    {
                        "id": "BX729091802",
                        "descriptor": {"name": "TLS Education Foundation"},
                        "categories": [
                            {
                                "id": "DSEP_CAT_7",
                                "descriptor": {"code": "pg", "name": "Post Graduate"},
                            }
                        ],
                        "fulfillments": [
                            {
                                "id": "DSEP_FUL_58081475",
                                "type": "SCHOLARSHIP",
                                "tracking": False,
                                "contact": {
                                    "phone": "9007216926",
                                    "email": "developer@tarkalabs.com",
                                },
                                "stops": [
                                    {
                                        "type": "APPLICATION-START",
                                        "time": {
                                            "timestamp": "2023-12-01T00:00:00.000Z"
                                        },
                                    },
                                    {
                                        "type": "APPLICATION-END",
                                        "time": {
                                            "timestamp": "2024-04-01T00:00:00.000Z"
                                        },
                                    },
                                ],
                            }
                        ],
                        "items": [
                            {
                                "id": "SCM_90576892",
                                "descriptor": {
                                    "name": "Tarka Labs Education Scholarship for Postgraduate Students",
                                    "long_desc": "Tarka Labs Education Scholarship for Postgraduate Students",
                                },
                                "price": {"currency": "INR", "value": "4500000"},
                                "rateable": True,
                                "tags": [
                                    {
                                        "display": True,
                                        "descriptor": {
                                            "code": "benefits",
                                            "name": "Benefits",
                                        },
                                        "list": [
                                            {
                                                "descriptor": {
                                                    "code": "scholarship-amount",
                                                    "name": "Scholarship Amount",
                                                },
                                                "value": "Upto Rs.45,00,000 per year",
                                                "display": True,
                                            }
                                        ],
                                    }
                                ],
                                "category_ids": ["DSEP_CAT_7"],
                                "fulfillment_ids": ["DSEP_FUL_58081475"],
                            }
                        ],
                        "rateable": True,
                    }
                ],
            }
        },
    }
]


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    print(f"received request body: {data} in /search")
    return jsonify(search_object)


@app.route("/client_callback", methods=["POST"])
def client_callback():
    print("Received a response for client_callback:", request.json)
    return jsonify({"message": "successful"})


if __name__ == "__main__":
    app.run(port=port, debug=True)
