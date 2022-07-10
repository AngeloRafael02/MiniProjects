const clientModule = require('../db');
const Route = require('express').Router();

Route.get("/all", async function (req,res) {
    try{
        clientModule.client.connect();
        client.characterCollection.find({material:"Freedom"}).sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
        clientModule.client.close();
    } catch(error){
        console.log(error);
    }
})