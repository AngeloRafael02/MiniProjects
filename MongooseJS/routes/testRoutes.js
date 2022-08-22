const testRoute = require('express').Router();
const User = require("../schema");
const mongooseClient = require('../client').mongooseClient

testRoute.get("/:name", async(req,res)=>{
    try{
        mongooseClient
        const response = await User.find({name:req.params.name})
        res.json(response)
        console.log(response)
    }catch(error){console.log(error)}
    mongooseClient
    
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

testRoute.patch('/:name', async (req,res)=>{
    try{
        mongooseClient
        await User.findOneAndUpdate({name:req.params.name},{name:req.body.name}, function (err,doc) {
                if (err) throw err;
                console.log(doc);
            });
        res.send("Update Successful")
    }catch(error){
        console.log(error);
    }
});

testRoute.delete('/:name', async (req,res)=>{
    try{
        mongooseClient
        const nameQuery = req.params.name
        await User.deleteOne({name:nameQuery},function(error){
            if(error) {throw error}
            else{ res.send(nameQuery + " has been Removed.")
            console.log(nameQuery + " has been Removed.")}
        })
    }catch(error){
        console.log(error);
    }
});

//NOTE:fix any thrown errors

module.exports = testRoute