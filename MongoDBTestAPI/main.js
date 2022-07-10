const express = require('express');
const customers = require('./routes/AllCharacterRoutes');

const app = express()

app.use('/characters', customers)

const PORT = process.env.PORT || 3000;
app.listen(PORT, function(){
    console.log(`App now running at LocalHost:${PORT}`);
})

