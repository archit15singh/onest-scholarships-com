const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  // Include information from the req object
  const responseData = {
    message: "Hello, World!",
    requestInfo: {
      method: req.method,
      url: req.url,
      headers: req.headers,
      // Include any other properties you want from the req object
    },
  };

  // Send the JSON stringified response
  res.send(JSON.stringify(responseData, null, 2)); // The third argument (2) is for pretty formatting
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
