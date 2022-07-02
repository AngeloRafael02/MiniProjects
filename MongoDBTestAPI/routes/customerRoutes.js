const client = require('../db')
const express = require('express');
const customerRoute = express.Router();

customerRoute.get("/", async function (req,res) {
    try{
        client.collection.find({}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
        });
    } catch(error){console.log(error)}
})

module.exports = customerRoute;
