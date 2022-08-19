const client = require('../db').client;
const Router = require('express').Router();
const RegionRouter = require('express').Router();
const AllCharacters = require('express').Router();

Router.get('/:name', async (req, res) => {
    const requestName =  req.params.name
    try{
        const response = await client.connect()
        response.db("GI_DB").collection('Characters')
            .find({name:requestName},{_id:0}).project({_id:0})
            .toArray(function(err, result) {
                if (err) throw err;
                res.json(result);
            }
        );
    }catch(err){
        console.log(err.stack);
    }
});

RegionRouter.get('/:region', async (req, res) => {
    const requestRegion =  req.params.region
    try{
        const response = await client.connect()
        response.db("GI_DB").collection('Characters')
            .find({region:requestRegion},{_id:0}).project({_id:0})
            .sort({star:1, name:1})
            .toArray(function(err, result) {
                if (err) throw err;
                res.json(result);
            }
        );
    }catch(err){
        console.log(err.stack);
    }
});

AllCharacters.get('/', async (req, res) => {
    try{
        const response = await client.connect()
        response.db("GI_DB").collection('Characters')
            .find({},{_id:0}).project({_id:0})
            .sort({region:1,star:1, name:1})
            .toArray(function(err, result) {
                if (err) throw err;
                res.json(result);
            }
        );
    }catch(err){
        console.log(err.stack);
    }
})

module.exports = {Router, RegionRouter,AllCharacters};

