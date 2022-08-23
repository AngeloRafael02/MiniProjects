const mongooseClient = require('./client').mongooseClient
const User = require("./schema");

const express = require('express');
const bodyParser = require('body-parser')
const app = express()

const testRoute = require('./routes/testRoutes')

app.use(bodyParser.json())

app.use("/test",testRoute)
app.get('/all',async(req,res)=>{
    try{
        mongooseClient
        const response = await User.find()
        res.json(response)
        console.log(response)
    }catch(error){console.log(error)}  
})

const PORT = process.env.PORT || 3000;
app.listen(PORT, function(){
    console.log(`listening at localhost:${PORT}, please wait for DB connection`)
})