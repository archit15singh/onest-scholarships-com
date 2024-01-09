const express = require("express");
const app = express();
const port = 4000;

app.use(express.json());

const items = {
  context: {
    domain: "onest:financial-support",
    action: "on_search",
    version: "1.1.0",
    bpp_id: "a8d2-2405-201-800b-c21a-2538-43c5-6514-4340.ngrok-free.app",
    bpp_uri:
      "https://a8d2-2405-201-800b-c21a-2538-43c5-6514-4340.ngrok-free.app/",
    country: "IND",
    city: "std:011",
    location: {
      city: {
        name: "New Delhi",
        code: "std:011",
      },
      country: {
        name: "India",
        code: "IND",
      },
    },
    transaction_id: "d4bbfcca-12c7-4e19-a540-b057a7c70009",
    message_id: "894310e5-8cb2-427d-ac28-c1cfc7551edc",
    ttl: "PT15M",
    timestamp: "2024-01-09T14:36:46.258Z",
  },
  message: {
    catalog: {
      descriptor: {
        name: "National Tarka Scholarship Portal - BPP Platform",
      },
      providers: [
        {
          id: "NSP213580001",
          descriptor: {
            name: "Indian Tarka Government Education Scholarship",
          },
          categories: [
            {
              id: "NSP_CAT_2",
              descriptor: {
                code: "ug",
                name: "Under Graduate",
              },
            },
          ],
          fulfillments: [
            {
              id: "NSP_FUL_64587601",
              type: "SCHOLARSHIP",
              tracking: false,
              contact: {
                phone: "9123456780",
                email: "scholarship@nsp.gov.in",
              },
              stops: [
                {
                  type: "APPLICATION-START",
                  time: {
                    timestamp: "2023-08-01T00:00:00.000Z",
                  },
                },
                {
                  type: "APPLICATION-END",
                  time: {
                    timestamp: "2023-11-30T00:00:00.000Z",
                  },
                },
              ],
            },
          ],
          items: [
            {
              id: "NSP_SCH_64587601",
              descriptor: {
                name: "Indian Tarka Government Scholarship for Undergraduate Students",
                long_desc:
                  "This scholarship aims to support meritorious postgraduate students across India.",
              },
              price: {
                currency: "INR",
                value: "30000",
              },
              rateable: false,
              tags: [
                {
                  display: true,
                  descriptor: {
                    code: "benefits",
                    name: "Benefits",
                  },
                  list: [
                    {
                      descriptor: {
                        code: "scholarship-amount",
                        name: "Scholarship Amount",
                      },
                      value: "Upto Rs.30000 per year",
                      display: true,
                    },
                  ],
                },
              ],
              category_ids: ["NSP_CAT_2"],
              fulfillment_ids: ["NSP_FUL_64587601"],
            },
          ],
          rateable: false,
        },
      ],
    },
  },
};

app.post("/client_callback", (req, res) => {
  res.status(200).json(items);
});

app.post("/on_subscribe", (req, res) => {
  res.status(200).send({ message: "Subscription successful" });
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
