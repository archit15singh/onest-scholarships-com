const express = require("express");
const app = express();
const port = 4000;

app.use(express.json());

const items = {
  context: {
    ttl: "PT10M",
    action: "search",
    timestamp: "2024-01-04T14:01:23.741Z",
    message_id: "d4e82f98-ef50-4d3b-9835-2c5d3b2c9c5e",
    transaction_id: "f2c4ec4a-22f8-4b8b-82fc-ef23d5f92b7d",
    domain: "onest:financial-support",
    version: "1.2.0",
    bap_id: "fs-ps-bap-network.onest.network",
    bap_uri: "https://fs-ps-bap-network.onest.network/",
    location: {
      city: {
        name: "Mumbai",
        code: "std:022",
      },
      country: {
        name: "India",
        code: "IND",
      },
    },
  },
  responses: [
    {
      context: {
        domain: "onest:financial-support",
        action: "on_search",
        version: "1.2.0",
        bpp_id: "beckn-sandbox-bpp.becknprotocol.io",
        bpp_uri: "https://sandbox-bpp-network.becknprotocol.io/",
        country: "IND",
        city: "std:022",
        location: {
          city: {
            name: "Mumbai",
            code: "std:022",
          },
          country: {
            name: "India",
            code: "IND",
          },
        },
        bap_id: "fs-ps-bap-network.onest.network",
        bap_uri: "https://fs-ps-bap-network.onest.network/",
        transaction_id: "f2c4ec4a-22f8-4b8b-82fc-ef23d5f92b7d",
        message_id: "d4e82f98-ef50-4d3b-9835-2c5d3b2c9c5e",
        ttl: "PT10M",
        timestamp: "2024-01-04T14:01:31.780Z",
      },
      message: {
        catalog: {
          descriptor: {
            name: "Aspire Higher Education Scholarship Platform",
          },
          providers: [
            {
              id: "HE205578912",
              descriptor: {
                name: "ABC Scholarship Foundation",
              },
              categories: [
                {
                  id: "DSEP_CAT_1",
                  descriptor: {
                    code: "ug",
                    name: "Under Graduate",
                  },
                },
              ],
              fulfillments: [
                {
                  id: "HE_FUL_84759301",
                  type: "GRANT",
                  tracking: true,
                  contact: {
                    phone: "9123456780",
                    email: "contact@abc-foundation.org",
                  },
                  stops: [
                    {
                      type: "APPLICATION-START",
                      time: {
                        timestamp: "2024-04-01T00:00:00.000Z",
                      },
                    },
                    {
                      type: "APPLICATION-END",
                      time: {
                        timestamp: "2024-06-30T00:00:00.000Z",
                      },
                    },
                  ],
                },
              ],
              items: [
                {
                  id: "GRANT_84759301",
                  descriptor: {
                    name: "ABC Postgraduate Research Grant",
                    long_desc:
                      "A grant aimed at supporting postgraduate research in science and technology fields.",
                  },
                  price: {
                    currency: "INR",
                    value: "50000",
                  },
                  rateable: false,
                  tags: [
                    {
                      display: true,
                      descriptor: {
                        code: "field-of-study",
                        name: "Field of Study",
                      },
                      list: [
                        {
                          descriptor: {
                            code: "study-area",
                            name: "Area of Study",
                          },
                          value: "Science and Technology",
                          display: true,
                        },
                      ],
                    },
                  ],
                  category_ids: ["HE_CAT_2"],
                  fulfillment_ids: ["HE_FUL_84759301"],
                },
              ],
              rateable: true,
            },
          ],
        },
      },
    },
  ],
};

function logRequestDetails(req, res, next) {
  console.log(`Received a request on ${req.path}`);
  console.log("Headers:", JSON.stringify(req.headers, null, 2));
  console.log("Query Parameters:", JSON.stringify(req.query, null, 2));
  console.log("Body:", JSON.stringify(req.body, null, 2));
  next();
}

app.use(logRequestDetails);

app.post("/client_callback", (req, res) => {
  res.status(200).json(items);
});

app.post("/on_subscribe", (req, res) => {
  res.status(200).send({ message: "Subscription successful" });
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
