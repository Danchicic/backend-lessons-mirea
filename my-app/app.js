var express = require("express");
var reload = require("express-reload");
var app = express();
app.get("/", (req, res) => {
    res.sendFile(`${__dirname}/index.html`);
})
var path = __dirname + '/app.js'
app.use(reload(path))
app.listen(3000, () => {
    console.log("Server started on port 3000");
})