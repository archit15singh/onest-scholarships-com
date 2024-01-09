const express = require("express");
const axios = require("axios");
const app = express();
const port = 3000;

app.use(express.json());

app.post("/on_subscribe", (req, res) => {
  console.log(
    "Received a subscription request:",
    JSON.stringify(req.body, null, 2)
  );
  res.status(200).send({ message: "Subscription successful" });
});

app.post("/client_callback", (req, res) => {
  console.log(
    "Received a request on client_callback:",
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

    console.log("got the data from /search", response.data);
    res.json(response.data);
  } catch (error) {
    console.error("Error calling external API", error);
    res.status(500).send("Error calling external API");
  }
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
