const express = require('express');
const cors = require("cors");
const app = express();
const PORT = 8080

app.use(
  cors({
    credentials: true,
    origin: ["http://localhost:3000"],
  })
)

var server = require('http').createServer(app)

server.listen(PORT, () => {
    console.log('Server listenig on port' + PORT);
})

app.get('/', (req, res)=> {
  res.sendStatus(200)
})
