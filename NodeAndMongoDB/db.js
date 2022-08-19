const {MongoClient} = require("mongodb");
const uri = "mongodb+srv://RecioAngeloRafael:XPWy77tpEFjHWuy@cluster0.cbzs3.mongodb.net/test";

const client = new MongoClient(uri);

module.exports = {client};