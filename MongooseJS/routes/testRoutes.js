const testRoute = require('express').Router();
const User = require("../schema");
const mongooseClient = require('../client').mongooseClient

testRoute.route('/:name')
    .get(async(req,res)=>{
        try{
            mongooseClient
            const response = await User.find({name:req.params.name})
            res.json(response)
            console.log(response)
        }catch(error){console.log(error)}    
    })
    .post(async(req,res)=>{
        try{
            mongooseClient
            const newUser = new User({
                name:req.params.name,
                age:req.body.age
                })
            await newUser.save()
            res.json(newUser)
            console.log(newUser.name + ' is saved')
        }catch(error){console.log(error)}
    })
    .patch(async(req,res)=>{
        try{
            mongooseClient
            await User.findOneAndUpdate(
                {name:req.params.name}, //filter
                {name:req.body.name} //update
                );
            res.send("Update Successful")
        }catch(error){console.log(error);}
    })
    .delete(async(req,res)=>{
        try{
            mongooseClient
            const nameQuery = req.params.name
            await User.deleteOne({name:nameQuery})
            res.send(nameQuery + " has been Removed.")
            console.log(nameQuery + " has been Removed.")
        }catch(error){console.log(error);}
    });

//NOTE:fix any thrown errors

module.exports = testRoute