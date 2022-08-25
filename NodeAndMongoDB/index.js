
const express = require('express');
const app = express();

const Router = require('./routes/CharacterRoutes').Router;
const RegionRouter = require('./routes/CharacterRoutes').RegionRouter;
const AllCharacters = require('./routes/CharacterRoutes').AllCharacters;
const CRUDRouter = require('./routes/CRUDRoute').CRUDRouter;
const AllUsersRoute = require('./routes/CRUDRoute').AllUsersRoute

app.use('/Characters', Router);
app.use('/Regions', RegionRouter);
app.use('/AllCharacters', AllCharacters);
app.use('/crud',CRUDRouter)
app.use('/testCRUD',AllUsersRoute)

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
})