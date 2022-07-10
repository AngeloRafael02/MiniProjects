const clientModule = require('../db')
const Route = require('express').Router();

Route.get("/all", async function (req,res) {
    try{
        clientModule.client.connect();
        client.characterCollection.find({}).sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
        clientModule.client.close()
    } catch(error){console.log(error)}
});
Route.get("/mondstadt", async function (req,res) {
    try{
        clientModule.client.connect();
        client.characterCollection.find({domain:"Forsaken Rift"}).sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
        clientModule.client.close()
    } catch(error){console.log(error)}
});
Route.get("/liyue", async function (req,res) {
    try{
        clientModule.client.connect();
        client.characterCollection.find({domain:"Taishan Mansion"}).sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
        clientModule.client.close()
    } catch(error){console.log(error)}
});
Route.get("/inazuma", async function (req,res) {
    try{
        client.client.connect();
        client.characterCollection.find({region:"Violet Court"}).sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
        client.client.close()
    } catch(error){console.log(error)}
});

module.exports = Route;
