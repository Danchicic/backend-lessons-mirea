var express = require("express");
var app = express();
const path = require("path");
app.use(express.static(path.join(__dirname)));


app.get("/", (req, res) => {
    res.sendFile(`${__dirname}/index.html`);
})
app.use((req, res)=> {
    res.status(404).sendFile(`${__dirname}/404.html`);
})
app.listen(8000, () => {
    console.log("Server started on port 8000");
})