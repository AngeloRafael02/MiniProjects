const express = require('express');
const customers = require('./routes/customerRoutes');

const app = express()

app.use('/customers', customers)

const PORT = process.env.PORT || 3000;
app.listen(PORT, function(){
    console.log(`App now running at LocalHost:${PORT}`);
})

