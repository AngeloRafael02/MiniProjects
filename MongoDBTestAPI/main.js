const express = require('express');
const allCharacterRoutes = require('./routes/AllCharacterRoutes');
const day1CharacterRoutes = require('./routes/Day1CharacterRoutes');
const day2CharactersRoutes = require('./routes/Day2CharacterRoutes');
const day3CharacterRoutes = require('./routes/Day3CharacterRoutes')

const app = express()

app.use('/allCharacters', allCharacterRoutes)
app.use('/day1characters', day1CharacterRoutes)
app.use('/day2characters', day2CharactersRoutes)
app.use('/day3characters', day3CharacterRoutes)

const PORT = process.env.PORT || 3000;
app.listen(PORT, function(){
    console.log(`App now running at LocalHost:${PORT}`);
})

