const express = require('express');
const bodyParser = require('body-parser')
const app = express()

const testRoute = require('./routes/testRoutes')

app.use(bodyParser.json())

app.use("/test",testRoute)

const PORT = process.env.PORT || 3000;
app.listen(PORT, function(){
    console.log(`listening at localhost:${PORT}`)
})