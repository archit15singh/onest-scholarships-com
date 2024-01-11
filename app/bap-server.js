const express = require("express");
const axios = require("axios");
const app = express();
const port = 3000;

function processResponse(data) {
  if (!data || !data.responses || !Array.isArray(data.responses)) {
    console.error("Invalid data structure");
    return;
  }

  data.responses.forEach((response) => {
    const providers = response.message?.catalog?.providers;
    if (!providers || !Array.isArray(providers)) {
      console.error("Invalid or missing providers array in response");
      return;
    }

    providers.forEach((provider) => {
      console.log(`Provider: ${provider.descriptor.name}`);
      provider.items.forEach((item) => {
        console.log(`  Scholarship Name: ${item.descriptor.name}`);
        console.log(`  Description: ${item.descriptor.long_desc}`);
        console.log(`  Amount: ${item.price.value} ${item.price.currency}`);
        item.tags.forEach((tag) => {
          console.log(`  Tag - ${tag.descriptor.name}:`);
          tag.list.forEach((listItem) => {
            console.log(`    ${listItem.descriptor.name}: ${listItem.value}`);
          });
        });
        console.log(
          `  Application Start: ${findDate(
            provider.fulfillments,
            "APPLICATION-START"
          )}`
        );
        console.log(
          `  Application End: ${findDate(
            provider.fulfillments,
            "APPLICATION-END"
          )}`
        );
        console.log("");
      });
    });
  });
}

function findDate(fulfillments, type) {
  if (!fulfillments || !Array.isArray(fulfillments)) {
    return "Not specified";
  }

  for (let fulfillment of fulfillments) {
    for (let stop of fulfillment.stops) {
      if (stop.type === type) {
        return new Date(stop.time.timestamp).toLocaleDateString();
      }
    }
  }
  return "Not specified";
}

function logRequestDetails(req, res, next) {
  console.log(`Received a request on ${req.path}`);
  console.log("Headers:", JSON.stringify(req.headers, null, 2));
  console.log("Query Parameters:", JSON.stringify(req.query, null, 2));
  console.log("Body:", JSON.stringify(req.body, null, 2));
  next();
}

app.use(express.json());

app.use(logRequestDetails);

app.post("/on_subscribe", (req, res) => {
  console.log(
    "Received a subscription request:",
    JSON.stringify(req.body, null, 2)
  );
  res.status(200).send({ message: "Subscription successful" });
});

app.post("/client_callback", (req, res) => {
  console.log(
    "Received a response for client_callback:",
    JSON.stringify(req.body, null, 2)
  );
  res.status(200).send({ message: "successful" });
});

app.post("/search", async (req, res) => {
  try {
    const requestData = {
      context: req.body.context,
      message: req.body.message,
    };

    const response = await axios.post(
      "http://localhost:5000/search",
      requestData
    );

    console.log(
      "got the data from /search",
      JSON.stringify(response.data, null, 2)
    );
    processResponse(response.data);
    res.json(response.data);
  } catch (error) {
    console.error("Error calling external API", error);
    res.status(500).send("Error calling external API");
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
