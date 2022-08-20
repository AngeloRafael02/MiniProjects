const express = require('express');

const app = express()

const mongoose = require('mongoose');    
mongoose.connect('mongodb+srv://RecioAngeloRafael:XPWy77tpEFjHWuy@cluster0.cbzs3.mongodb.net/?retryWrites=true&w=majority',
    ()=>{ console.log("Connected to Database by mongooseJS")},
    e => console.error(e)
)