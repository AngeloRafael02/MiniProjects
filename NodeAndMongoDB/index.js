
const express = require('express');
const app = express();

const Router = require('./routes/CharacterRoutes').Router;
const RegionRouter = require('./routes/CharacterRoutes').RegionRouter;

app.use('/Characters', Router);
app.use('/Regions', RegionRouter);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
})