const client = require('../db');
const Router = require('express').Router();
const RegionRouter = require('express').Router();

//NOTE: Fix the sorting of the characters by region
Router.get('/:name', async (req, res) => {
    const requestName =  req.params.name
    try{
        client.connect().then(async function(){
            const response = await client.connect()
            response.db("GI_DB").collection('Characters').find({name:requestName})
                .toArray(function(err, result) {
                    if (err) throw err;
                    res.json(result);
                }
            );
        });
    }catch(err){
        console.log(err.stack);
    }
});

RegionRouter.get('/:region', async (req, res) => {
    const requestRegion =  req.params.region
    try{
        client.connect().then(async function(){
            const response = await client.connect()
            response.db("GI_DB").collection('Characters').find({region:requestRegion})
                .toArray(function(err, result) {
                    if (err) throw err;
                    res.json(result);
                }
            );
        });
    }catch(err){
        console.log(err.stack);
    }
});

module.exports = {Router, RegionRouter};

