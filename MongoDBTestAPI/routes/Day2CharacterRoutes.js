const client = require('../db')
const Route = require('express').Router();

Route.get("/all", async function (req,res) {
    try{
        client.characterCollection.find({availability:['Sunday','Tuesday','Friday']})
            .sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
    } catch(error){console.log(error)}
});
Route.get("/mondstadt", async function (req,res) {
    try{
        client.characterCollection.find({material:"Resistance"})
            .sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
    } catch(error){console.log(error)}
});
Route.get("/liyue", async function (req,res) {
    try{
        client.characterCollection.find({material:"Diligence"})
            .sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
    } catch(error){console.log(error)}
});
Route.get("/inazuma", async function (req,res) {
    try{
        client.characterCollection.find({material:"Elegance"})
            .sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
    } catch(error){console.log(error)}
});

module.exports = Route;
