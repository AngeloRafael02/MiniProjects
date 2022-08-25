const client = require('../db').CRUDConnect;
const CRUDRouter = require('express').Router();
const AllUsersRoute = require('express').Router();

CRUDRouter.route("/:name")
    .get(async(req,res)=>{
        const requestName = req.params.name
        try{
            const response = client
            response.find({name:requestName},{_id:0})
                .project({_id:0})
                .toArray(function (err,result) {
                    if (err) throw err;
                    res.json(result)
                });
        }catch(error){console.log(error)}
    })
    .post(async(req,res)=>{
        try{
            client
            const newUser = {
                name:req.params.name,
                age:18
            }
            await client.insertOne(newUser)
                .then((err,result)=>{
                    if (err)throw err;
                    console.log("Added: " + result.name)
                });
            res.send(newUser.name + " has been Added");
        }catch(error){console.log(error)}
    })
    .patch(async(req,res)=>{
        try{
            await client.updateOne(
                {name:req.params.name},
                {$set:{name:"Daniel"}}
            )
            console.log("Update Successfully");
            res.send("Update Successfully")
        }catch(error){console.log(error)}     
    })
    .delete(async(req,res)=>{
        try{
            await client.deleteOne(
                {name:req.params.name}
            )
            console.log("Deleted " + req.params.name)
            res.send("Deleted " + req.params.name)
        }catch(error){console.log(error)}
    });

AllUsersRoute.get('/',(req,res)=>{
        try{
            const response = client
            response.find()
                .toArray(function (err,result) {
                    if (err) throw err;
                    res.json(result)
                });
        }catch(error){console.log(error)}
})

module.exports = {CRUDRouter,AllUsersRoute}