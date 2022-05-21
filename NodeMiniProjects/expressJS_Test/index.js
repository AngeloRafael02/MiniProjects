const express = require('express');
const app = express();
const path = require('path');
const router = express.Router();


router.get('/',function(req,res){
    res.sendFile(path.join(__dirname + '/FrontEnd/index.html'));
});

router.get('/view',function(req,res){
    res.sendFile(path.join(__dirname + '/FrontEnd/view.html'));
})

router.get('/view1',function(req,res){
    res.sendFile(path.join(__dirname + '/FrontEnd/view1.html'));
})

app.use('/',router);
app.listen(process.env.port || 3000);
console.log("Running at Port:3000")