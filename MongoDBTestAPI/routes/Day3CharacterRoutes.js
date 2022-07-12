const client = require('../db')
const Route = require('express').Router();

Route.get("/all", async function (req,res) {
    try{
        client.characterCollection.find({availability:['Sunday','Wednesday','Saturday']})
            .sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
    } catch(error){console.log(error)}
});
Route.get("/mondstadt", async function (req,res) {
    try{
        client.characterCollection.find({availability:['Sunday','Wednesday','Saturday'], material:"Ballad"})
            .sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
    } catch(error){console.log(error)}
});
Route.get("/liyue", async function (req,res) {
    try{
        client.characterCollection.find({availability:['Sunday','Wednesday','Saturday'], material:"Gold"})
            .sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
    } catch(error){console.log(error)}
});
Route.get("/inazuma", async function (req,res) {
    try{
        client.characterCollection.find({availability:['Sunday','Wednesday','Saturday'], material:"Light"})
            .sort({star:1, name:1}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
    } catch(error){console.log(error)}
});

module.exports = Route;
