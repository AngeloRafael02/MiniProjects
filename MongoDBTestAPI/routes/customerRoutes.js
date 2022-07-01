const express = require('express');
const customerRoute = express.Router(),
      { MongoClient } = require("mongodb");

const uri = "mongodb+srv://RecioAngeloRafael:XPWy77tpEFjHWuy@cluster0.cbzs3.mongodb.net/?retryWrites=true&w=majority"
const client = new MongoClient(uri);

customerRoute.get("/", async function (req,res) {
    try{
        await client.connect();
        const database = client.db('testDB');
        const customers = database.collection('customers');
        customers.find({}).toArray(function (err,result) {
            if (err) throw err;
            res.json(result);
            client.close();
        });
    } catch(error){console.log(error)}
})

module.exports = customerRoute;