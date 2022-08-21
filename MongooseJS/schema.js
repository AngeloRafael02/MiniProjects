const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema({
    name:String,
    age:Number
})

module.exports =  mongoose.model("User",UserSchema) //model function has 2 main arguments (name of  model, Schema)
// the schema is also the collection