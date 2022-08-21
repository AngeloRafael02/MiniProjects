const testRoute = require('express').Router();
const User = require("../schema");
const mongooseClient = require('../client').mongooseClient

testRoute.get("/:name", async(req,res)=>{
    mongooseClient
    const response = await User.find({name:req.params.name})
    res.json(response)
    console.log(response)
});

testRoute.post("/", async (req,res)=>{
    try{
        mongooseClient
        const newUser = new User({
            name:req.body.name,
            age:req.body.age
            })
        await newUser.save()
        res.json(newUser)
        console.log(newUser.name + ' is saved')
    }catch(error){
        console.log(error)
    }
});

//NOTE:Make PATCH adn DELETE requests

module.exports = testRoute