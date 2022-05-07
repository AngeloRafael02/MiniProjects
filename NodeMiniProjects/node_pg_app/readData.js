const {pool}  = require("./db");

async function readData(){
    try{
        const read = await pool.query(
            "SELECT * FROM table1"
        );
        console.log(read.rows);
    } catch(error){
        console.log(error);
    }
}

readData();