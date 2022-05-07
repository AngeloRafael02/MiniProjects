const {Pool} = require('pg');

const pool = new Pool({
    user:'test',
    password:'password',
    database:'test',
    port: 5432,
    host:'localhost',
})

module.exports = {pool};