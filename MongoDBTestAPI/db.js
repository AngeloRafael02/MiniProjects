const { MongoClient } = require("mongodb");

const uri = "mongodb+srv://RecioAngeloRafael:XPWy77tpEFjHWuy@cluster0.cbzs3.mongodb.net/?retryWrites=true&w=majority"
const client = new MongoClient(uri);
client.connect();

const database = client.db('GI_DB');
const collection = database.collection('Characters');

module.exports = {client,collection}