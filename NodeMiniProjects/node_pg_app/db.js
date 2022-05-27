const {Pool} = require('pg');

const pool = new Pool({ //this mean that the Role was already made in pg. 
    user:'test',
    password:'password',
    database:'test',
    port: 5432,
    host:'localhost',
})

module.exports = {pool};